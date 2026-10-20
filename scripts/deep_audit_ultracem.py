import urllib.request
import re
import json
from collections import Counter

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

# 1. Download and parse main CSS
css_url = "https://ultracem.co/wp-content/litespeed/css/5006a9ad86d7f6ade2b261ac322d2c69.css?ver=df691"
print(f"Fetching CSS from {css_url}...")
try:
    req = urllib.request.Request(css_url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as resp:
        css_text = resp.read().decode('utf-8', errors='ignore')
except Exception as e:
    print(f"Error fetching CSS: {e}")
    css_text = ""

print(f"CSS length: {len(css_text)} bytes")

# Extract all hex colors
hex_colors = re.findall(r'#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b', css_text)
hex_colors = ['#' + c.upper() for c in hex_colors]
# Filter out common neutrals (pure white/black/grays) to find the brand colors
neutral_list = ['#FFFFFF', '#FFF', '#000000', '#000', '#F0F0F0', '#FAFAFA', '#F7F8F9', '#CCCCCC', '#CCC', '#333333', '#333', '#666666', '#222222', '#32373C', '#4F4F4F', '#3F3F3F', '#3A3A3A', '#595959', '#606060', '#BFBFBF']
brand_colors = [c for c in hex_colors if c not in neutral_list]
print("\n--- BRAND COLORS IN CSS ---")
top_brand = Counter(brand_colors).most_common(20)
for c, cnt in top_brand:
    print(f"  {c}: {cnt}")

# Extract rgb / rgba colors
rgba_colors = re.findall(r'rgba?\(\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)', css_text)
rgba_common = Counter([f"rgb({r},{g},{b})" for r, g, b in rgba_colors]).most_common(10)
print("\n--- RGB COLORS IN CSS ---")
for rgb, cnt in rgba_common:
    print(f"  {rgb}: {cnt}")

# Extract fonts in CSS
fonts_css = re.findall(r'font-family:\s*([^;\}!]+)', css_text)
cleaned_fonts = []
for f in fonts_css:
    f_clean = f.strip().strip('"\'')
    if len(f_clean) > 2 and 'inherit' not in f_clean:
        cleaned_fonts.append(f_clean)
print("\n--- FONTS IN CSS ---")
for f, cnt in Counter(cleaned_fonts).most_common(10):
    print(f"  {f}: {cnt}")

# 2. Scrape additional subpages for complete product catalogue and brand info
pages = [
    ("Nosotros", "https://ultracem.co/nosotros/"),
    ("Cementos", "https://ultracem.co/cementos/"),
    ("Concretos", "https://ultracem.co/concretos/"),
    ("Morteros", "https://ultracem.co/morteros-secos/")
]

subpage_data = {}
for p_name, p_url in pages:
    try:
        req = urllib.request.Request(p_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as r:
            p_html = r.read().decode('utf-8', errors='ignore')
            # Extract title and headings
            h_tags = re.findall(r'<h[1-3][^>]*>(.*?)</h[1-3]>', p_html, re.DOTALL)
            h_clean = [re.sub(r'<[^>]+>', '', h).strip() for h in h_tags if len(h.strip()) > 2]
            # Extract images
            p_imgs = re.findall(r'https://ultracem\.co/wp-content/uploads/[^\s\"\'\>\<\)]+', p_html)
            subpage_data[p_name] = {
                "url": p_url,
                "headings": h_clean[:15],
                "images": list(set([img.split('?')[0] for img in p_imgs]))[:10]
            }
            print(f"Scraped {p_name}: {len(h_clean)} headings, {len(p_imgs)} images")
    except Exception as e:
        print(f"Could not scrape {p_name} ({p_url}): {e}")

# Save comprehensive brand audit
brand_audit = {
    "brand_name": "ULTRACEM",
    "legal_name": "Ultracem S.A.S.",
    "website": "https://ultracem.co/",
    "taglines": [
        "Venta de Cemento y Concreto",
        "Soluciones integrales para la industria de la construcción",
        "Calidad, Resistencia y Rendimiento",
        "Soluciones innovadoras para la construcción",
        "Ahora comprar productos Ultracem es mucho más fácil"
    ],
    "ai_assistant": {
        "name": "Vanesa",
        "channel": "WhatsApp",
        "concept": "Autogestión con IA en un sector tradicional: Vanesa y la apuesta de Ultracem por una relación cada vez más inteligente"
    },
    "training_program": {
        "name": "Campus Ultra WhatsApp",
        "concept": "La apuesta de Ultracem por la formación del sector de la construcción"
    },
    "headquarters_and_plants": {
        "main_plant": "Galapa, Atlántico, Colombia",
        "other_countries": ["Colombia", "Guatemala"]
    },
    "commercial_advisors_contacts": [
        {"name": "Hichel Espitia", "phone": "3102503454"},
        {"name": "Milena Ospino", "phone": "3135574297", "email": "mospino@ultracem.co"},
        {"name": "Adriana Anaya", "phone": "3207096744", "email": "aanaya@ultracem.co"},
        {"customer_service": "servicioalcliente@ultracem.co"}
    ],
    "logos": {
        "main_logo_blue": "https://ultracem.co/wp-content/uploads/2020/04/logo-ultracem-azul-e1693862120398.webp",
        "logo_mobile": "https://ultracem.co/wp-content/uploads/2019/02/Cemento-Concreto-ultracem-Logo-Mobile.webp",
        "logo_footer_yellow": "https://ultracem.co/wp-content/uploads/2019/02/logo-amarillo-footer.png",
        "favicon": "https://ultracem.co/wp-content/uploads/2020/05/Favicon-logo-ultracem.jpg",
        "gemas_brandmark": "https://ultracem.co/wp-content/uploads/2020/04/gemas@2x.png"
    },
    "color_palette": {
        "primary_blue": "#003E78", # Used in links, titles, brand identity
        "cobalt_blue": "#004797", # Used in primary action buttons, headers
        "ultracem_yellow_accent": "#FCB900", # Used in yellow footer logo and highlights
        "accent_vivid_orange": "#FF6900", # Used in product ribbons and badges
        "accent_blue": "#1E73BE", # Used in hover and secondary highlights
        "dark_navy_slate": "#222222",
        "pure_white": "#FFFFFF",
        "light_slate_bg": "#F7F8F9"
    },
    "typography": {
        "primary_family": "Montserrat, sans-serif",
        "secondary_system": "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
        "weights": ["300 (Light)", "400 (Regular)", "600 (SemiBold)", "700 (Bold)", "900 (Black)"]
    },
    "social_networks": {
        "facebook": "https://www.facebook.com/CementoUltracem/",
        "instagram": "https://www.instagram.com/cementoultracem/",
        "linkedin": "https://co.linkedin.com/company/ultracem",
        "youtube": "https://www.youtube.com/channel/UCAiiV-YyfjEZQdY7fneSAvg",
        "twitter": "https://twitter.com/Ultracem",
        "tiktok": "https://www.tiktok.com/@cementoultracem"
    },
    "subpages": subpage_data
}

with open("d:/Documentos/CARPETA IMPORTANTE/PROGRAMACION/COOWEB/assets/ultracem_brand_audit.json", "w", encoding="utf-8") as f:
    json.dump(brand_audit, f, indent=2, ensure_ascii=False)

print("\n--- BRAND AUDIT COMPLETED & SAVED TO assets/ultracem_brand_audit.json ---")
