
import datetime
import logging

import ccxt
from config import LogInfo
from db_tools.write_symbol_to_db import df_to_db
from info_from_site.bibox_symbols import get_symbol_df
from fetch_data.fetch_trades import get_trade_df


def trade_job():
    time_now = datetime.datetime.utcnow()
    try:
        symbol = 'BIX/USDT'
        table_name = symbol.lower().replace('/', '_')
        df = get_trade_df()
        df_to_db(df, table_name, LogInfo.conn)
        print(f"get dat {df}")
        print(f"Insert {table_name} to db by Bing Li and the time is {str(time_now)}")
    except ccxt.base.errors.RequestTimeout:
        print("Getting data failed, will retry in next minute!")


if __name__ == "__main__":
    df = get_trade_df()
    symbol = 'BIX/USDT'
    table_name = symbol.lower().replace('/', '_')
    df_to_db(df, table_name, LogInfo.conn)
    print(df)
