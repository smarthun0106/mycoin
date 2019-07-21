import pybithumb
import time
import datetime
import pandas as pd

con_key = "2163f13eba4bb94c2484ee067e85e4aa"
sec_key = "1a3464c32c915b13fefb76210c879ac2"
bithumb = pybithumb.Bithumb(con_key, sec_key)

def get_target_price(ticker, k):
    df = pybithumb.get_ohlcv(ticker)
    yesterday = df.iloc[-2]

    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    target = today_open + (yesterday_high - yesterday_low) * k
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
    ma3 = close.rolling(3).mean()
    return ma5[-2], ma3[-2]

def auto_trading(ticker, k):
    now = datetime.datetime.now()
    mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
    current_price = pybithumb.get_current_price(ticker)
    target_price = get_target_price(ticker, k)
    ma5, ma3 = get_yesterday_ma5(ticker)
    df = pd.DataFrame(columns=['date', 'buy', 'sell', 'ror'])
    count = 0
    while True:
        try:
            now = datetime.datetime.now()
            balance = bithumb.get_balance(ticker)[0]
            current_price = pybithumb.get_current_price(ticker)

            con1 = mid < now < mid + datetime.timedelta(seconds=10)
            con2 = balance > 0.001
            if  con1 and con2:
                target_price = get_target_price(ticker, k)
                mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
                ma5 = get_yesterday_ma5(ticker)
                sell_crypto_currency(ticker)
                print("매도완료! CP: {0}, TP: {1}, MA5: {2}".format(current_price, target_price, ma5))
                sell_price = current_price
                df.loc[count] = [now.date()] + [buy_price] + [sell_price]
                df.loc[count, 'ror'] = np.round(sell_price/buy_price, 3)
                df.to_csv('result.csv', mode='a', header=False)
                count = count + 1

            con1 = (current_price > target_price)
            con2 = (current_price > ma5)
            con3 = balance < 0.001
            if con1 and con2 and con3 :
                buy_crypto_currency(ticker)
                print("매수완료! CP: {0}, TP: {1}, MA5: {2}".format(current_price, target_price, ma5))

                buy_price = current_price
                df = df.append({'date': now.date(),
                            'buy' : current_price}, ignore_index=True)

        except:
            print('에러발생')
        time.sleep(1.5)

if __name__ == '__main__':
    ticker = input("ticker : ")
    k = float(input("k : "))
    print("ticker: {0}, k: {1}".format(ticker, k))
    auto_trading(ticker, k)
