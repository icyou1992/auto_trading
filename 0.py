###
# import requests
# import datetime
# r = requests.get("https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw")

# bitcoin = r.json()
# timestamp = bitcoin['timestamp']
# date = datetime.datetime.fromtimestamp(timestamp/1000)

# print(bitcoin)
# print(date)

###
# from pandas import DataFrame

# data = {"open": [858, 854], "high": [544, 665], "low": [800, 605], "close": [210, 322]}
# df = DataFrame(data, index=["2017-01-01", "2017-01-02"])

# print(df)

###
# import pandas as pd
# import requests

# url = "https://finance.naver.com/item/sise_day.nhn?code=066570"
# df = pd.read_html(requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text)

# print(df[0])


