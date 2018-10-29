
import datetime
import logging

import ccxt
from config import LogInfo
from db_tools.write_symbol_to_db import df_to_db
from fetch_data.fetch_trades import get_trade_df, get_latest_trade_from_db


def trade_job():
    time_now = datetime.datetime.utcnow()
    try:
        symbol = 'BIX/USDT'
        table_name = symbol.lower().replace('/', '_') + '_trade'
        df = get_trade_df(symbol)
        df = df.drop(columns=["info"])
        last = get_latest_trade_from_db(table_name, LogInfo.conn)
        db_latest_id = last["id"][0]
        new_df = df[df['id'] > int(db_latest_id)]
        print(len(new_df))
        print(db_latest_id)
        df_to_db(new_df, table_name, LogInfo.conn)
        print(f"Insert {table_name} to db by Bing Li and the time is {str(time_now)}")
    except ccxt.base.errors.RequestTimeout:
        print("Getting data failed, will retry in next minute!")


if __name__ == "__main__":
    df = get_trade_df()
    symbol = 'BIX/USDT'
    table_name = symbol.lower().replace('/', '_') + '_trade'
    df = df.drop(columns=["info"])
    print(table_name)
    df_to_db(df, table_name, LogInfo.conn)
    print(df)
