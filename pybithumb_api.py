import pybithumb
import numpy as np
import math

con_key = "2163f13eba4bb94c2484ee067e85e4aa"
sec_key = "1a3464c32c915b13fefb76210c879ac2"

bithumb = pybithumb.Bithumb(con_key, sec_key)


''' 잔고조회 '''
# 비트코인 총잔고, 거래중인 비트코인의 수량, 보유 중인 총원화 튜플값으로 반환
# balance = bithumb.get_balance("BTC")
# print(balance)
# print(format(balance[0], 'f')) # 단위 수정

''' 매수 '''
def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

krw = bithumb.get_balance('BTC')[2]

orderbook = pybithumb.get_orderbook("XRP")
asks = orderbook['asks']
sell_price = asks[4]['price']
unit = krw / sell_price
print(unit)
# order = bithumb.buy_limit_order("XRP", 4000000, 0.001) # 지정가 매수
order = bithumb.buy_market_order("XRP", unit) #시장가 매수
print(order)
