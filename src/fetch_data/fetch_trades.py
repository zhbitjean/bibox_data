import ccxt
import pandas as pd
from config import DBInfo


def get_trade_df(symbol='BIX/USDT'):
    api = DBInfo.api
    ccxt_client = ccxt.bibox(api)
    # api only give 200 records from current time
    trade_data = ccxt_client.fetch_trades(symbol)
    trade_df = pd.DataFrame(trade_data)
    trade_df['id'] = trade_df['id'].astype('int64')
    return trade_df


if __name__ == "__main__":
    symbol = 'BIX/USDT'
    symbol_name = symbol.lower().replace('/', '_')
    # table_name = 'bibox_trade'
    # conn = DBInfo.conn
    # df = get_recent_records(table_name, conn, limit=10)
    # print(df)
    # ccxt_client = ccxt.bibox(api)
    # symbol = 'BIX/USDT'
    # data = ccxt_client.fetch_trades(symbol, limit=300)
    # df = pd.DataFrame(data)
    # df.to_csv("trades.csv")
