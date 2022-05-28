from bs4 import BeautifulSoup
import urllib.request as req

# 通貨設定
crypto = 'BTC'
currency = 'JPY'

# スクレイピングページ
url = 'https://coinyep.com/ja/ex/' + crypto + '-' + currency

# 取得結果
current_value = ''

# 取得先URLにアクセス
res = req.urlopen(url)

# 対象を抽出
soup = BeautifulSoup(res, 'html.parser');
values = soup.select_one("#coinyep-reverse1").findAll(text=True)
current_value = str(''.join(values))
current_value = current_value.replace('1 ' + crypto + ' = ', '')
current_value = current_value.replace(' ' + currency, '')

# 取得結果
print('1' + crypto + '(' + currency + '): ' + str(current_value))