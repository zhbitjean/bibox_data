import pandas as pd
import time
import ccxt
import json

def get_symbol_trade_df():
    """
    BiboxAPI: https://github.com/Biboxcom/API_Docs/wiki
    ccxt: https://github.com/ccxt/ccxt/
    """

    api = {"apiKey": 'eeccea338ecb24b796497f82765ba8ab71561d52',
           "secret": '5f7e2c9bd79ca6b3a7676ff7cdc6765e6d1c68ac'}

    ccxt_client = ccxt.bibox(api)
    symbol = 'BIX/GUSD'
    interval = '1d'

    symbol_l = ccxt_client.fetch_ohlcv(symbol, interval)
    bibox_index = [
        'date',
        'Open',
        'High',
        'Low',
        'Close',
        'Volume'
    ]
    symbol_df = pd.DataFrame(symbol_l, columns=bibox_index)

    symbol_df['date'] = symbol_df['date'].astype('datetime64[ms]')
    symbol_df['mean_volume'] = symbol_df['Volume']
    symbol_df = symbol_df.set_index(['date'])
    symbol_df.to_csv('symbol_org.csv')
    df = symbol_df.copy()
    df = df.rolling(min_periods=1, window=7).mean()
    df.to_csv('symbol_mean.csv')
    df = df.reset_index()
    print(df)
    return df


if __name__ == "__main__":
    api = {"apiKey": 'eeccea338ecb24b796497f82765ba8ab71561d52',
           "secret": '5f7e2c9bd79ca6b3a7676ff7cdc6765e6d1c68ac'}

    ccxt_client = ccxt.bibox(api)
    symbol = 'BIX/GUSD'
    data = ccxt_client.fetch_trades(symbol)
    print(ccxt_client.fetch_trades(symbol))
    print(len(ccxt_client.fetch_trades(symbol)))
    print(type(data))
    df = pd.DataFrame(data)
    df.to_csv("trades.csv")
    # json = json.dumps(data)
    # for var in json:
    #     print(type(var))
    # if ccxt_client.has['fetchTrades']:
    #     ccxt_client_markets = ccxt_client.load_markets()
    #     for symbol in ccxt_client.markets:  # ensure you have called loadMarkets() or load_markets() method.
    #         time.sleep (ccxt_client.rateLimit / 1000)  # time.sleep wants seconds
    #         print (symbol, ccxt_client.fetch_trades (symbol))
