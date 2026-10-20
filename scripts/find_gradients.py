import re

with open('scripts/build_ultraracha_v3.py', 'r', encoding='utf-8') as f:
    text = f.read()

gradients = re.findall(r'bg-gradient-[a-zA-Z0-9\-_/]+', text)
print(f'Total bg-gradient found: {len(gradients)}')
print('Set of gradients:', set(gradients))

linear_grad = re.findall(r'linear-gradient\([^)]+\)', text)
print(f'Total linear-gradient found: {len(linear_grad)}')
print('Set of linear-gradient:', set(linear_grad))
