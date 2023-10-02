import json

import requests

cookies = {
    'mda': '0',
    'gdpr': '0',
    '_ym_uid': '16935235128056879',
    'yandexuid': '9844611741680726682',
    'yuidss': '9844611741680726682',
    'i': 'gGAiI2vU/Rt4cpeJEf+6hK/k0VWnL6O6UWWURSEsjgtsj8gP1hgpkOr+IptZ201/PKCqzkrMB169Yafc2UMS0pYqkio=',
    'ymex': '1696527452.oyu.4296435011693521336#2008883512.yrts.1693523512',
    'is_gdpr': '0',
    'is_gdpr_b': 'COj6IhDszQEoAg==',
    'yandex_gid': '18',
    '_ym_isad': '2',
    '_ym_d': '1696261884',
    'cycada': 'wHY9yUqCBUMOQtcwdnvjnuMqRn8vKTfpx5HS8/0aMGA=',
    'device_id': 'b2eb57ceec7b872d52167e25977d9061715d8b84f',
    '_ym_visorc': 'b',
    'ys': 'wprid.1696262552334666-244907585311944138-balancer-l7leveler-kubr-yp-vla-88-BAL-9025#c_chck.3050535871',
    'yp': '1698940071.hdrc.0#2011622535.pcs.0#1698768493.ygu.1#1696262893.nwcst.1696179000_18_1#1696866469.szm.1:1920x1080:1920x948',
    'bh': 'Ej8iR29vZ2xlIENocm9tZSI7dj0iMTEzIiwiQ2hyb21pdW0iO3Y9IjExMyIsIk5vdC1BLkJyYW5kIjt2PSIyNCIaBSJ4ODYiIg8iMTEzLjAuNTY3Mi45MiIqAj8wOgciTGludXgiQgciNi4yLjAiSgQiNjQiUloiR29vZ2xlIENocm9tZSI7dj0iMTEzLjAuNTY3Mi45MiIsIkNocm9taXVtIjt2PSIxMTMuMC41NjcyLjkyIiwiTm90LUEuQnJhbmQiO3Y9IjI0LjAuMC4wIiI=',
    '_yasc': 'YpzwnHbHuuzMlM6+uMUck2EuCebUBIlc5pxt7nMRBHLUR4UuTaHQttrT7e7uvNGusa0mpTXXQTKSRcfl9GXA',
    'spravka': 'dD0xNjk2MjYyNzg2O2k9ODUuMTc0LjE5Mi4yMTU7RD1ERkNDNzcyMTZDRTUxN0QzREE3Mjg4ODg3Q0U1M0JDM0VEQzdDREU3Qzk2RkUzMEY0Mjg4QTdGRDM1QzIxNzhDOUJEMkU5MTFBNTFDMjYxRDQ0OEJFMkU1MjBBRjJFRTBBN0FENzdEM0RGNTQxOEQzNTMzNkJGNEM1OUVGRUNFOTA5RUNBOTQxNzc1QUU2ODc2NzNERkY4OUU0QkRFMDBFO3U9MTY5NjI2Mjc4NjMxMzE4OTk0MztoPTdlOGMwMDlmYjM5MDJmY2EyOGNiZmRmOTE4YTBkMGVi',
    'active-browser-timestamp': '1696262768437',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    # 'Cookie': 'mda=0; gdpr=0; _ym_uid=16935235128056879; yandexuid=9844611741680726682; yuidss=9844611741680726682; i=gGAiI2vU/Rt4cpeJEf+6hK/k0VWnL6O6UWWURSEsjgtsj8gP1hgpkOr+IptZ201/PKCqzkrMB169Yafc2UMS0pYqkio=; ymex=1696527452.oyu.4296435011693521336#2008883512.yrts.1693523512; is_gdpr=0; is_gdpr_b=COj6IhDszQEoAg==; yandex_gid=18; _ym_isad=2; _ym_d=1696261884; cycada=wHY9yUqCBUMOQtcwdnvjnuMqRn8vKTfpx5HS8/0aMGA=; device_id=b2eb57ceec7b872d52167e25977d9061715d8b84f; _ym_visorc=b; ys=wprid.1696262552334666-244907585311944138-balancer-l7leveler-kubr-yp-vla-88-BAL-9025#c_chck.3050535871; yp=1698940071.hdrc.0#2011622535.pcs.0#1698768493.ygu.1#1696262893.nwcst.1696179000_18_1#1696866469.szm.1:1920x1080:1920x948; bh=Ej8iR29vZ2xlIENocm9tZSI7dj0iMTEzIiwiQ2hyb21pdW0iO3Y9IjExMyIsIk5vdC1BLkJyYW5kIjt2PSIyNCIaBSJ4ODYiIg8iMTEzLjAuNTY3Mi45MiIqAj8wOgciTGludXgiQgciNi4yLjAiSgQiNjQiUloiR29vZ2xlIENocm9tZSI7dj0iMTEzLjAuNTY3Mi45MiIsIkNocm9taXVtIjt2PSIxMTMuMC41NjcyLjkyIiwiTm90LUEuQnJhbmQiO3Y9IjI0LjAuMC4wIiI=; _yasc=YpzwnHbHuuzMlM6+uMUck2EuCebUBIlc5pxt7nMRBHLUR4UuTaHQttrT7e7uvNGusa0mpTXXQTKSRcfl9GXA; spravka=dD0xNjk2MjYyNzg2O2k9ODUuMTc0LjE5Mi4yMTU7RD1ERkNDNzcyMTZDRTUxN0QzREE3Mjg4ODg3Q0U1M0JDM0VEQzdDREU3Qzk2RkUzMEY0Mjg4QTdGRDM1QzIxNzhDOUJEMkU5MTFBNTFDMjYxRDQ0OEJFMkU1MjBBRjJFRTBBN0FENzdEM0RGNTQxOEQzNTMzNkJGNEM1OUVGRUNFOTA5RUNBOTQxNzc1QUU2ODc2NzNERkY4OUU0QkRFMDBFO3U9MTY5NjI2Mjc4NjMxMzE4OTk0MztoPTdlOGMwMDlmYjM5MDJmY2EyOGNiZmRmOTE4YTBkMGVi; active-browser-timestamp=1696262768437',
    'Referer': 'https://music.yandex.ru/chart',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}


params = {
    'what': 'chart',
    'lang': 'ru',
    'external-domain': 'music.yandex.ru',
    'overembed': 'false',
    'ncrnd': '0.4346034032624708',
}

response = requests.get('https://music.yandex.ru/handlers/main.jsx', params=params, cookies=cookies, headers=headers).json()

with open('chart.json', 'w') as f:
    json.dump(response, f, indent=4, ensure_ascii=False)

with open('chart.json', 'r') as f:
    chart = json.load(f)

all_songs = dict()
for ind, inform in enumerate(chart['chartPositions']):
    song = inform['track']
    all_songs[ind+1] = {tuple([artist['name']
                                      for artist in song['artists']]): song['title']}

print(all_songs)
