import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/build_ultraracha_v3.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Locate phone frame
start_marker = '<!-- Phone Canvas Frame:'
end_marker = '<!-- ============================================================== -->\n    <!-- 2. VISTA SUPERVISOR WEB'

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

print("start_idx:", start_idx)
print("end_idx:", end_idx)

phone_snippet = text[start_idx:end_idx].strip()
print("Phone snippet length:", len(phone_snippet))
print("Last 150 chars of phone snippet:")
print(phone_snippet[-150:])
