''' 변동성 돌파 전략 백테스팅 '''
import pybithumb
import pandas as pd
import numpy as np

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', 19)
pd.set_option('display.width', 210)

def range_stretagy_01(year, ticker, k=None, ma_k=None):
    try:
        df = pybithumb.get_ohlcv(ticker)
        df = df[str(year)]

        df['ma'] = df['close'].rolling(window=ma_k).mean().shift(1)
        df['bull'] = df['open'] > df['ma']

        df['range'] = (df['high'] - df['low']) * k
        df['target'] = df['open'] + df['range'].shift(1)

        fee = 0.0032
        # ror
        df['ror'] = np.where((df['high'] > df['target']) & df['bull'],
                             df['close']/df['target'] - fee,
                             1)
        df['hpr'] = df['ror'].cumprod()

        #MDD
        df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
        return df['hpr'][-2], df['dd'].max()

    except:
        pass




tickers = pybithumb.get_tickers()
table = pd.DataFrame()
ma_k = [3, 5]
y = '2019-05'
for ticker in tickers:
    for ma in ma_k:
        for k in np.arange(0.1, 1.0, 0.1):
            try:
                ror, mdd = range_stretagy_01(y, ticker, k=k, ma_k=ma)
                print("가상화폐:{0}, k값:{1:.1f}, ror:{2:.6f}, mdd:{3:.0f}, ma:{4}".format(ticker, k, ror, mdd, ma))
                columns = {
                    '년도' : y, '가상화폐' : ticker,
                    'k값' : k, 'ma' : ma,
                    'ror' : ror, 'mdd' : mdd
                }
                table = table.append(columns, ignore_index=True)
            except:
                pass
table = table[['년도', '가상화폐', 'k값', 'ma', 'ror', 'mdd']]
table.to_excel("btc_"+ y +".xlsx")


''' 변동성 돌파 k값 '''
# import pybithumb
# import numpy as np
#
# def get_ror(k=0.5):
#     df = pybithumb.get_ohlcv("BTC")
#     df = df['2019']
#     df['range'] = (df['high'] - df['low']) * k
#     df['target'] = df['open'] + df['range'].shift(1)
#
#     fee = 0.0032
#     df['ror'] = np.where(df['high'] > df['target'],
#                          df['close']/df['target'] - fee,
#                          1)
#
#     ror = df['ror'].cumprod()[-2]
#     return ror
#
# for k in np.arange(0.1, 1.0, 0.1):
#     ror = get_ror(k)
#     print("%.1f %f" % (k, ror))

''' 상승장 전략 백테스팅 '''
# import pybithumb
# import numpy as np
#
# df = pybithumb.get_ohlcv('ETC')
# df = df['2019']
# df['ma5'] = df['close'].rolling(window=3).mean().shift(1)
# df['bull'] = df['open'] > df['ma5']
# df['target'] = df['open'] * 1.03
# df['bull2'] = df['target'] < df['high']
# fee = 0.0032
# df['ror'] = np.where(df['bull2'], df['target'] / df['open'] - fee, 1)
# df['hpr'] = df['ror'].cumprod()
# print(df['hpr'][-2])
# df.to_excel("btc.xlsx")



''' 변동성 돌파 + 상승장 전략 백테스팅'''
# import pybithumb
# import numpy as np
#
# def get_hpr(ticker):
#     try:
#         df = pybithumb.get_ohlcv(ticker)
#         df = df['2019']
#         df['ma5'] = df['close'].rolling(window=5).mean().shift(1)
#         df['range'] = (df['high'] - df['low']) * 0.5
#         df['target'] = df['open'] + df['range'].shift(1)
#         df['bull'] = df['open'] > df['ma5']
#
#         fee = 0.0032
#         df['ror'] = np.where((df['high'] > df['target']) & df['bull'],
#                          df['close']/df['target'] - fee,
#                          1)
#
#         df['hpr'] = df['ror'].cumprod()
#         df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
#
#         return df['hpr'][-2], df['dd'].max()
#     except:
#         return 1
#
# tickers = pybithumb.get_tickers()
# hprs = []
# for ticker in tickers:
#     hpr, dd = get_hpr(ticker)
#     hprs.append((ticker, hpr, dd))
#
# sorted_hprs = sorted(hprs, key=lambda x:x[1], reverse=True)
# print(sorted_hprs[:5])
