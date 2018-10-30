import ccxt
import pandas as pd
import datetime
import time
from config import DBInfo
from db_tools.write_symbol_to_db import write_symbol_to_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_tools.read_from_db import read_df_from_db


def get_trade_df(symbol='BIX/USDT'):
    api = DBInfo.api
    ccxt_client = ccxt.bibox(api)
    # api only give 200 records from current time
    trade_data = ccxt_client.fetch_trades(symbol)
    trade_df = pd.DataFrame(trade_data)
    trade_df['id'] = trade_df['id'].astype('int64')
    print(trade_df)
    return trade_df


def get_latest_trade_from_db(table_name, conn):
    sql_db = pd.io.sql.SQLDatabase(conn)
    query = f"SELECT * FROM {table_name} WHERE id IN (SELECT MAX(id) FROM {table_name})"
    if not sql_db.has_table(table_name):
        return None
    else:
        obj = pd.read_sql(query, conn)
    return obj


if __name__ == "__main__":
    symbol = 'BIX/USDT'
    table_name = symbol.lower().replace('/', '_') + '_trade'
    # print(df_to_db)
    # api = LogInfo.api
    # ccxt_client = ccxt.bibox(api)
    # symbol = 'BIX/USDT'
    # data = ccxt_client.fetch_trades(symbol, limit=300)
    # df = pd.DataFrame(data)
    # df.to_csv("trades.csv")
