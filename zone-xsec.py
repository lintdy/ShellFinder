import requests
import re
from tqdm import tqdm

for page in tqdm(range(0, 50), desc="Progress"):
    r = requests.get(f"https://zone-xsec.com/archive/page={page}")
    preg = re.findall(r'<td>([a-zA-Z0-9.-]+)', r.text)
    for domain in preg:
        if re.match(r'[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', domain):
            domain = re.sub(r'..co.', '.com', domain)
            open('zone-xsec.com.txt', 'a').write(f'{domain}\n')
            