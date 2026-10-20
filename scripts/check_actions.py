import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/build_ultraracha_v3.py', 'r', encoding='utf-8') as f:
    text = f.read()

keywords = ['openVoiceNotesModal', 'escalarCasoSLA', 'enviarConsultaAI', 'openTransferClientModal', 'abrirWhatsAppCliente']
for kw in keywords:
    pos = text.find(kw)
    print(f"{kw}: pos {pos}")
    if pos != -1:
        print(text[pos:pos+200])
        print("---")
