import pybithumb
import time
import datetime

''' 현재 빗썸에 등록된 코인 리스트 출력 '''
# tickers = pybithumb.get_tickers()
# print(tickers)

''' 해당 코인 현재 가격 출력 '''
# price = pybithumb.get_current_price('BTC')
# print(price)

''' 저가/고가/평균거래금액/거래량 출력'''
# detail = pybithumb.get_market_detail('BTC') # 저가/고가/평균거래금액/거래량
# print(detail)

''' 해당코인의 timestamp, payment_currency, order_currency, bids, asks를 dic으로 반환 '''
# orderbook = pybithumb.get_orderbook("BTC")
# print(orderbook['payment_currency']) # 화폐단위
# print(orderbook['order_currency'])  # 코인목록
# print(orderbook['bids']) # 매수호가창
# print(orderbook['asks']) # 매도 호가창
#
# # timestamp를 datetime를 통해 변환
# ms = int(orderbook['timestamp'])
# dt = datetime.datetime.fromtimestamp(ms/1000)
# print(dt)

''' 2013년~ 과거 데이터 출력 '''
# btc = pybithumb.get_ohlcv("BTC")
# print(btc)

''' 해당코인 과거 데이터 기반으로 이평선구하기 '''
# btc = pybithumb.get_ohlcv("BTC")
# close = btc['close']
#
# window = close.rolling(5)
# ma5 = window.mean()
# print(ma5)
