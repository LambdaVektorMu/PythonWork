# coding: utf-8

import warnings
import requests
from bs4 import BeautifulSoup

warnings.filterwarnings('ignore')  # warningが出ないようにする

# ブログより記事のタイトルの文字列を取得する

url_blog = 'https://tech-diary.net/python-scraping-books/'  # ブログの対象の記事のURL
response = requests.get(url_blog)

soup = BeautifulSoup(response.text)  # レスポンスから取得したHTMLデータを設定する
print(soup.find('h1').text)  # ブログの記事のタイトルを表示する
