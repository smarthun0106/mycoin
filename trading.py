import pybithumb
import time
import datetime

con_key = "2163f13eba4bb94c2484ee067e85e4aa"
sec_key = "1a3464c32c915b13fefb76210c879ac2"
bithumb = pybithumb.Bithumb(con_key, sec_key)

def get_target_price(ticker):
    df = pybithumb.get_ohlcv(ticker)
    yesterday = df.iloc[-2]

    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    target = today_open + (yesterday_high - yesterday_low) * 0.5
    return target

def buy_crypto_currency(ticker):
    krw = bithumb.get_balance(ticker)[2]
    orderbook = pybithumb.get_orderbook(ticker)
    sell_price = orderbook['asks'][0]['price']
    unit = krw/float(sell_price)
    bithumb.buy_market_order(ticker, unit)

def sell_crypto_currency(ticker):
    unit = bithumb.get_balance(ticker)[0]
    bithumb.sell_market_order(ticker, unit)

def get_yesterday_ma5(ticker):
    df = pybithumb.get_ohlcv(ticker)
    close = df['close']
    ma5 = close.rolling(5).mean()
    return ma5[-2]

def auto_trading(ticker):
    now = datetime.datetime.now()
    mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
    target_price = get_target_price(ticker)
    ma5 = get_yesterday_ma5(ticker)

    while True:
        try:
            now = datetime.datetime.now()
            if mid < now < mid + datetime.timedelta(seconds=10):
                target_price = get_target_price(ticker)
                mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
                ma5 = get_yesterday_ma5(ticker)
                sell_crypto_currency(ticker)
                print("매도완료! CP: {0}, TP: {1}, MA5: {2}".format(current_price, target_price, ma5))

            current_price = pybithumb.get_current_price(ticker)
            if (current_price > target_price) and (current_price > ma5):
                buy_crypto_currency(ticker)
                print("매수완료! CP: {0}, TP: {1}, MA5: {2}".format(current_price, target_price, ma5))
        except:
            print('에러발생')
        time.sleep(1)

if __name__ == '__main__':
    auto_trading("BTC")
