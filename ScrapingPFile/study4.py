# coding: utf-8

import warnings
import requests
from bs4 import BeautifulSoup

warnings.filterwarnings('ignore')  # warningが出ないようにする

url_python = 'https://www.python.org/'
respones = requests.get(url_python)
soup = BeautifulSoup(respones.text)

# spanタグの情報を全て取得する
span_tag_list = soup.find_all('span', class_='say-no-more')
print(len(span_tag_list))
print(span_tag_list)
# 複数クラス指定
span_tag_list = soup.find_all('span', class_=['say-no-more', 'message'])
print(len(span_tag_list))
print(span_tag_list)

# 辞書式でクラスの指定も可能
span_class_list = soup.find_all('span', {'class': 'say-no-more'})
print(len(span_class_list))
print(span_class_list)
span_class_list = soup.find_all('span', {'class': ['say-no-more', 'message']})
print(len(span_class_list))
print(span_class_list)
