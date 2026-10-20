with open('scripts/build_ultraracha_v3.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
funcs = re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', text)
print(f"Total JS functions: {len(funcs)}")
print("Sample functions:", funcs[:30])
