import urllib.request
import re
import json
from bs4 import BeautifulSoup
from collections import Counter

url = "https://ultracem.co/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
req = urllib.request.Request(url, headers=headers)

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
except Exception as e:
    print(f"Error fetching: {e}")
    html = ""

print(f"Fetched {len(html)} bytes from {url}")

soup = BeautifulSoup(html, 'html.parser')

# 1. Metadata & Slogans
meta_desc = soup.find('meta', attrs={'name': 'description'})
og_title = soup.find('meta', attrs={'property': 'og:title'})
og_desc = soup.find('meta', attrs={'property': 'og:description'})
og_image = soup.find('meta', attrs={'property': 'og:image'})
twitter_site = soup.find('meta', attrs={'name': 'twitter:site'})

print("\n--- METADATA & BRAND PROMISES ---")
print("Page Title:", soup.title.string if soup.title else "")
print("Meta Description:", meta_desc['content'] if meta_desc else "")
print("OG Title:", og_title['content'] if og_title else "")
print("OG Description:", og_desc['content'] if og_desc else "")
print("OG Image:", og_image['content'] if og_image else "")

# 2. Extract Headings (h1, h2, h3, h4)
headings = []
for tag in soup.find_all(['h1', 'h2', 'h3', 'h4']):
    text = tag.get_text(strip=True)
    if text and len(text) > 2:
        headings.append((tag.name, text))

print(f"\n--- HEADINGS ({len(headings)}) ---")
for h_type, h_text in headings[:25]:
    print(f"[{h_type.upper()}] {h_text}")

# 3. Extract Images & Logos
img_tags = soup.find_all('img')
logos = []
product_imgs = []
all_imgs = []

for img in img_tags:
    src = img.get('src') or img.get('data-src') or img.get('srcset') or ''
    alt = img.get('alt', '')
    if not src or src.startswith('data:image'):
        continue
    all_imgs.append((src, alt))
    src_lower = src.lower()
    alt_lower = alt.lower()
    if 'logo' in src_lower or 'logo' in alt_lower or 'favicon' in src_lower:
        logos.append((src, alt))
    elif any(k in src_lower or k in alt_lower for k in ['cemento', 'concreto', 'mortero', 'saco', 'bulto', 'producto']):
        product_imgs.append((src, alt))

print(f"\n--- LOGOS & ICONOGRAPHY ({len(logos)}) ---")
for src, alt in list(set(logos))[:15]:
    print(f"Logo: {src} | Alt: {alt}")

print(f"\n--- PRODUCT IMAGES ({len(product_imgs)}) ---")
for src, alt in list(set(product_imgs))[:15]:
    print(f"Product: {src} | Alt: {alt}")

# 4. Color Palette Extraction (from CSS styles, attributes, inline styles)
css_links = [link['href'] for link in soup.find_all('link', rel='stylesheet') if 'href' in link.attrs]
print(f"\n--- CSS FILES ({len(css_links)}) ---")
for l in css_links[:5]:
    print("CSS:", l)

hex_colors = re.findall(r'#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b', html)
hex_colors = ['#' + c.upper() for c in hex_colors]
color_counts = Counter(hex_colors).most_common(20)

print(f"\n--- TOP DETECTED HEX COLORS ---")
for color, count in color_counts:
    print(f"{color}: {count} occurrences")

# 5. Font Families
fonts = re.findall(r'font-family:\s*([^;\}]+)', html)
font_counts = Counter([f.strip().strip('"\'') for f in fonts]).most_common(10)
print(f"\n--- DETECTED FONTS ---")
for font, count in font_counts:
    print(f"{font}: {count} occurrences")

# 6. Contact Information & Social Links
social_links = []
for a in soup.find_all('a', href=True):
    href = a['href']
    if any(s in href.lower() for s in ['facebook', 'instagram', 'linkedin', 'twitter', 'youtube', 'tiktok', 'whatsapp', 'tel:', 'mailto:']):
        social_links.append((a.get_text(strip=True), href))

print(f"\n--- SOCIAL & CONTACT LINKS ({len(social_links)}) ---")
for txt, href in list(set(social_links))[:15]:
    print(f"Link: {txt} -> {href}")

# Save full extraction to JSON
branding_data = {
    "site": "https://ultracem.co/",
    "title": soup.title.string if soup.title else "",
    "meta_description": meta_desc['content'] if meta_desc else "",
    "og_title": og_title['content'] if og_title else "",
    "og_description": og_desc['content'] if og_desc else "",
    "og_image": og_image['content'] if og_image else "",
    "headings": headings,
    "logos": list(set(logos)),
    "product_images": list(set(product_imgs)),
    "top_colors": [c[0] for c in color_counts],
    "fonts": [f[0] for f in font_counts],
    "social_links": list(set(social_links))
}

with open("d:/Documentos/CARPETA IMPORTANTE/PROGRAMACION/COOWEB/assets/ultracem_branding_extracted.json", "w", encoding="utf-8") as f:
    json.dump(branding_data, f, indent=2, ensure_ascii=False)

print("\nSuccessfully saved extracted branding to assets/ultracem_branding_extracted.json")
