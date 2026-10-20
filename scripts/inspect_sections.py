import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/build_ultraracha_v3.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos_header_toggle = text.find('<!-- View Toggle')
print("pos_header_toggle:", pos_header_toggle)
if pos_header_toggle != -1:
    print(text[pos_header_toggle:pos_header_toggle+800])

pos_main = text.find('<main id="main-content"')
print("\npos_main:", pos_main)
pos_phone_start = text.find('<!-- Phone Canvas Frame:', pos_main)
print("pos_phone_start:", pos_phone_start)
pos_view_web = text.find('id="view-web"', pos_main)
print("pos_view_web:", pos_view_web)
pos_main_end = text.find('</main>', pos_main)
print("pos_main_end:", pos_main_end)
