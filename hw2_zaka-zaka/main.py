import json
from time import sleep
import requests
from bs4 import BeautifulSoup

cookies = {
    'PHPSESSID': 'tgjir52npj5v1hkp06ifith72r',
    '51a55dae53577255b792d39bfe1d40ac': '0',
    '_ga': 'GA1.1.1588027250.1696263736',
    '_ym_uid': '1696263737646169240',
    '_ym_d': '1696263737',
    '_ym_isad': '2',
    '_ga_BB3QC8QLF4': 'GS1.1.1696263736.1.1.1696264088.0.0.0',
}

headers = {
    'authority': 'zaka-zaka.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'PHPSESSID=tgjir52npj5v1hkp06ifith72r; 51a55dae53577255b792d39bfe1d40ac=0; _ga=GA1.1.1588027250.1696263736; _ym_uid=1696263737646169240; _ym_d=1696263737; _ym_isad=2; _ga_BB3QC8QLF4=GS1.1.1696263736.1.1.1696264088.0.0.0',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
}

games = {}

def get_page_url(num):
    return 'https://zaka-zaka.com/game/new/page{}'.format(num)

def game_info(block):
    name = block.find('div', class_='game-block-name').text
    price = block.find('div', class_='game-block-price').text[:-2]
    return name, price

def s_page(num):
    print('Cтраница {}'.format(num))
    response = requests.get(get_page_url(num), cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    blocks = soup.find_all('a', class_='game-block')
    
    for block in blocks:
        if 'game-block-more' in block.get('class'):
            continue
        name, price = game_info(block)
        games[name] = price

for i in range(1, 16):
    s_page(i)

with open('games.json', 'w') as file:
    json.dump(games, file, indent=4)
