#!/home/l_vektor_m/PythonWork/ScrapingStudy/bin/python3
# coding: utf-8

# SUUMOのHPから物件データを取得する
# 複数件の物件情報を得る

import warnings
from pprint import pprint

import requests
from bs4 import BeautifulSoup

warnings.filterwarnings('ignore')  # warningが出ないようにする

# SUUMOのサイトのURL（埼玉県八潮市の賃貸情報）
url_yashio = 'https://suumo.jp/chintai/saitama/sc_yashio/?page={}'
# ページ番号を付随させたURL
target_url = url_yashio.format(1)
response = requests.get(target_url)
soup = BeautifulSoup(response.text)

contents = soup.find_all('div', {'class': 'cassetteitem'})
print(len(contents))

# 現在HPに表示されている部屋情報のリスト
room_list = []

for c in contents:
    # 物件情報クラス：cassetteitem-detail
    detail = c.find('div', {'class': 'cassetteitem-detail'})
    # 物件名
    title = detail.find('div', {'class': 'cassetteitem_content-title'}).text
    # 住所
    address = detail.find('li', {'class': 'cassetteitem_detail-col1'}).text
    # アクセス情報
    access = detail.find('li', {'class': 'cassetteitem_detail-col2'}).text
    # 築年数
    age = detail.find('li', {'class': 'cassetteitem_detail-col3'}).text

    # 物件情報の辞書
    detail_dic = {
        'title': title,
        'address': address,
        'access': access,
        'age': age
    }

    # 各部屋情報クラス：cassetteitem_other
    table = c.find('table', {'class': 'cassetteitem_other'})
    tr_tags = table.find_all('tr', {'class': 'js-cassette_link'})

    for tr_t in tr_tags:
        # HPの表から必要な部分だけを抜き出す
        floor, price, first_fee, capacity = tr_t.find_all('td')[2:6]

        fee, management_fee = price.find_all('li')
        deposit, gratuity = first_fee.find_all('li')
        madori, menseki = capacity.find_all('li')

        # 部屋情報の辞書
        room_dic = {
            'floor': floor.text,
            'fee': fee.text,
            'management_fee': management_fee.text,
            'deposit': deposit.text,
            'gratuity': gratuity.text,
            'madori': madori.text,
            'menseki': menseki.text
        }

        room_list.append({**detail_dic, **room_dic})

pprint(room_list[0])
print()
pprint(room_list[1])
