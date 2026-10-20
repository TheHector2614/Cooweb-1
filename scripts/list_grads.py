import re

with open('scripts/build_ultraracha_v3.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'bg-gradient' in line or 'gradient' in line:
        print(f"Line {i+1}: {line.strip()[:100]}")
