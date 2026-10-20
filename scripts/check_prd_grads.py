import re

with open('scripts/generate_prd_html.py', 'r', encoding='utf-8') as f:
    text = f.read()

grads = re.findall(r'bg-gradient-[a-zA-Z0-9\-_/]+', text)
print('Gradients in generate_prd_html.py:', len(grads), set(grads))
