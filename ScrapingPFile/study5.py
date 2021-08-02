# coding: utf-8

import warnings
import requests
from bs4 import BeautifulSoup
from requests.api import delete

warnings.filterwarnings('ignore')  # warningが出ないようにする

# SUUMOのサイトのURL
url_yashio = 'https://suumo.jp/chintai/saitama/sc_yashio/?page={}'
# ページ番号を付随させたURL
target_url = url_yashio.format(1)
response = requests.get(target_url)
soup = BeautifulSoup(response.text)

contents = soup.find_all('div', {'class': 'cassetteitem'})
print(len(contents))

content0 = contents[0]
# 物件情報クラス：cassetteitem-detail
detail = content0.find('div', {'class': 'cassetteitem-detail'})
# 物件名
title = detail.find('div', {'class': 'cassetteitem_content-title'}).text
# 住所
address = detail.find('li', {'class': 'cassetteitem_detail-col1'}).text
# アクセス情報
access = detail.find('li', {'class': 'cassetteitem_detail-col2'}).text
# 築年数
age = detail.find('li', {'class': 'cassetteitem_detail-col3'}).text
print(title, address, access, age)

# 各部屋情報クラス：cassetteitem_other
table = content0.find('table', {'class': 'cassetteitem_other'})
tr_tags = table.find_all('tr', {'class': 'js-cassette_link'})
tr_tag0 = tr_tags[0]

# 賃料・管理費
price_rent = tr_tag0.find('span', {'class': 'cassetteitem_price cassetteitem_price--rent'}).text
price_administration = tr_tag0.find('span', {'class': 'cassetteitem_price cassetteitem_price--administration'}).text
# 敷金・礼金
price_deposit = tr_tag0.find('span', {'class': 'cassetteitem_price cassetteitem_price--deposit'}).text
price_gratuity = tr_tag0.find('span', {'class': 'cassetteitem_price cassetteitem_price--gratuity'}).text
# 間取り・面積
layout = tr_tag0.find('span', {'class': 'cassetteitem_madori'}).text
area = tr_tag0.find('span', {'class': 'cassetteitem_menseki'}).text
print(price_rent, price_administration, price_deposit, price_gratuity, layout, area)

""" a = tr_tag0.find_all('span', {'class': ['cassetteitem_price cassetteitem_price--rent',
                                    'cassetteitem_price cassetteitem_price--administration',
                                    'cassetteitem_price cassetteitem_price--deposit',
                                    'cassetteitem_price cassetteitem_price--gratuity',
                                    'cassetteitem_madori',
                                    'cassetteitem_menseki']})
print(a) """

target_items = tr_tag0.find_all('td')[2:6]
print(target_items)
