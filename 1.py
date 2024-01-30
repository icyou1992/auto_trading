import pyupbit
import os
import time
import datetime

upbit = pyupbit.Upbit(os.environ["access_key"], os.environ["secret_key"])
print(upbit.get_balance())

tickers = pyupbit.get_tickers(fiat="KRW", verbose=False, is_details=False)
print(tickers)

btc = "KRW-BTC"
eth = "KRW-ETH"
dot = "KRW-DOT"
eos = "KRW-EOS"

krw = upbit.get_balances()
print(krw)
# orderbook = pyupbit.get_orderbook(btc)

###
# price = pyupbit.get_current_price(["KRW-BTC", "KRW-ETH"])
# print(price)
# df = pyupbit.get_ohlcv(btc)
# print(df)
# orderbook = pyupbit.get_orderbook(btc)
# print(orderbook)

# ret = upbit.buy_limit_order(btc, "61938000", 0.0001)
# print(ret)

###
# tier = 0
# while True:
#   tier += 1
#   price = pyupbit.get_current_price(btc)  
#   time.sleep(0.2)
#   print(price)
#   if tier > 30:
#     break

###
# df = pyupbit.get_ohlcv(btc)

# yesterday = df.iloc[-2]

# today_open = yesterday['close']

# yesterday_high = yesterday['high']
# yesterday_low = yesterday['low']

# target = today_open + (yesterday_high - yesterday_low) * 0.5
# print(target)


###
# dt = datetime.datetime(2018, 12, 1)

# print(dt)
# print(dt.year, dt.month, dt.day)

# now = datetime.datetime.now()
# mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
# print(now)
# print(mid)

# print(now == dt)
# print(now > dt)


# def get_target_price(ticker):
#   df = pyupbit.get_ohlcv(ticker)
#   yesterday = df.iloc[-2]

#   today_open = yesterday['close']
#   yesterday_high = yesterday['high']
#   yesterday_low = yesterday['low']
#   target = today_open + (yesterday_high - yesterday_low) * 0.5
#   return target

# now = datetime.datetime.now()
# mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)

# target_price = get_target_price(btc)

# while True:
#   now = datetime.datetime.now()
#   if mid < now < mid + datetime.timedelta(seconds=10):
#     target_price = get_target_price(btc)
#     mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)

#   current_price = pyupbit.get_current_price(btc)
#   print(current_price)

#   time.sleep(1)


###
# print(orderbook)
# while True:
#   now = datetime.datetime.now()
#   if mid < now < mid + datetime.timedelta(seconds=10):
#     target_price = get_target_price(btc)
#     mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
  
#   current_price = pyupbit.get_current_price(btc)
#   if current_price > target_price:
#     krw = pyupbit.get_balances()
#     orderbook = pyupbit.get_orderbook(btc)

#     print(orderbook)


###
df = pyupbit.get_ohlcv(btc)
close = df['close']
ma5 = close.rolling(5).mean()

print(ma5)



  




