with open('scripts/build_ultraracha_v3.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(?i)(?:semillero|cooweb)', text)
print(f"Total occurrences of semillero/cooweb: {len(matches)}")
