import ccxt
import pandas as pd
import datetime
import time
from config import LogInfo


def get_trade_df(symbol='BIX/USDT'):
    api = LogInfo.api
    ccxt_client = ccxt.bibox(api)
    # api only give 200 records from current time
    trade_data = ccxt_client.fetch_trades(symbol)
    trade_df = pd.DataFrame(trade_data)
    print(trade_df)
    return trade_df


if __name__ == "__main__":
    api = LogInfo.api
    ccxt_client = ccxt.bibox(api)
    symbol = 'BIX/USDT'
    data = ccxt_client.fetch_trades(symbol, limit=300)
    df = pd.DataFrame(data)
    df.to_csv("trades.csv")
