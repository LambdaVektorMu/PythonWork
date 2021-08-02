# coding: utf-8

import warnings
import requests
from bs4 import BeautifulSoup

warnings.filterwarnings('ignore')  # warningが出ないようにする

url_python = 'https://www.python.org'
respones = requests.get(url_python)

soup = BeautifulSoup(respones.text)

# h2タグから文字列リストを作成する
h2_tag_text_list = []
for i, h2_tag in enumerate(soup.find_all('h2')):
    print(i, h2_tag.text)
    h2_tag_text_list.append(h2_tag.text)

print(h2_tag_text_list)

# リスト内包表記でh2タグの文字列リストを作る
x = [t.text for t in soup.find_all('h2')]
print(x)
