# coding: utf-8

import warnings
import requests
from bs4 import BeautifulSoup

warnings.filterwarnings('ignore')  # warningが出ないようにする

# ブログより記事のタイトルの文字列を取得する

url_blog = 'https://tech-diary.net/python-scraping-books/'  # ブログの対象の記事のURL
response = requests.get(url_blog)
soup = BeautifulSoup(response.text)

caption_list = soup.find_all(['h2', 'h3'])
print(len(caption_list))
for l in caption_list:
    print(l)

# 記事の本文はarticleタグにあるのでそこの範囲から情報を取得する
caption_article_list = soup.find('article').find_all(['h2', 'h3'])
print(len(caption_article_list))
for t in caption_article_list:
    print(t.text)

# 記事本文を予め変数に格納しておく
body = soup.find('article')
h2h3_tag_list = body.find_all(['h2', 'h3'])
print(len(h2h3_tag_list))
for t in h2h3_tag_list:
    print(t.text)
