with open('scripts/build_ultraracha_v3.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos_act = text.find('INTERACTIVE ACTIVATION BAR')
print("pos_act:", pos_act)
if pos_act != -1:
    print(text[pos_act-50:pos_act+800])
