# Welcome to kusa-bot
このレポジトリでは、github actionsを用いてpushを定期実行します。

# Actions Flow
- 09:00(JST)にcronジョブが起動
- blank.ymlに従ってpythonファイル(btc_jpy.py)を実行
- btc/jpyの09:00(JST)の値段をwebサイトからスクレイピング
- 取得した値段をREADME.mdに書き込み保存

# Everyday BTC/JPY at 09:00(JST)
<br>2022-05-28 1BTC(JPY): 3691661<br>2022-05-28 1BTC(JPY): 3691661
