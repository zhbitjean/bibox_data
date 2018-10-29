import datetime
import logging

import ccxt
from config import DBInfo
from db_tools.write_symbol_to_db import df_to_db
from fetch_data.fetch_trades import get_trade_df, get_latest_trade_from_db
from jobs.utils.logUtils import LogInfo


def job_detail():
    time_now = datetime.datetime.utcnow()
    symbol = 'BIX/USDT'
    table_name = 'bibox_trade'
    symbol_name = symbol.lower().replace('/', '_')
    df = get_trade_df(symbol)
    df = df.drop(columns=["info"])
    df["symbol"] = symbol_name
    start_time = datetime.datetime.fromtimestamp(df['timestamp'][0] / 1000.0)
    end_time = datetime.datetime.fromtimestamp(list(df['timestamp'])[-1] / 1000.0)
    start_id = int(df['id'][0])
    end_id = int(list(df['id'])[-1])
    last = get_latest_trade_from_db(table_name, DBInfo.conn)
    db_latest_id = last["id"][0]
    new_df = df[df['id'] > int(db_latest_id)]
    new_record_count = len(new_df)
    print(new_record_count)
    print(db_latest_id)
    df_to_db(new_df, table_name, DBInfo.conn)
    print(time_now)
    msg = f"Insert {table_name} to db by Bing Li and the time is {str(time_now)}."
    updateRecord = LogInfo(log_time=time_now,
                           start_time=start_time,
                           end_time=end_time,
                           start_id=start_id,
                           end_id=end_id,
                           new_record_count=new_record_count,
                           message=msg)
    # add_new_log(DBInfo.conn, time_now, time_now, time_now, 110, 111, 23, msg)
    print(type(time_now))
    print(type(start_time))
    print(type(end_time))
    print(type(start_id))
    print(type(end_time))
    print(type(new_record_count))
    updateRecord.add_new_log(DBInfo.conn)
    print(msg)


def trade_job():
    try:
        job_detail()
    except:
        print("Getting data failed, will retry in next minute!")


if __name__ == "__main__":
    job_detail()
