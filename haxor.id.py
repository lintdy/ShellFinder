import re
import requests
from tqdm import tqdm

for page in tqdm(range(0, 50), desc="Progress"):
    url = f'https://haxor.id/archive?page={page}'
    response = requests.get(url)
    html_content = response.text
    pattern = re.compile(r'href=["\'](https?://.*?)["\']')
    matches = pattern.findall(html_content)
    if matches:
        for href_value in matches:
            href_value = re.sub(r'^https?://', '', href_value)
            href_value = re.sub(r'/.*', '', href_value)
            open('haxor.id.txt', 'a').write(f'{href_value}\n')
    else:
        pass
