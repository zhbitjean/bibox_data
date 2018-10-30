import datetime
import logging

import ccxt
from config import DBInfo
from db_tools.write_symbol_to_db import df_to_db
from fetch_data.fetch_trades import get_trade_df
from db_tools.read_from_db import get_latest_trade_from_db, get_recent_records
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
    db_df = get_recent_records(table_name, DBInfo.conn)
    api_ids = set(list(df['id']))
    db_ids = set(list(db_df['id']))
    overlap_ids = api_ids.intersection(db_ids)
    overlap_count = len(overlap_ids)
    if last is not None:
        db_latest_id = last["id"][0]
        new_df = df[df['id'] > int(db_latest_id)]
        new_record_count = len(new_df)
    else:
        new_df = df
        new_record_count = len(df)
    if overlap_count > 0:
        overlap_msg = f"Getting {overlap_count} overlap records."
    else:
        overlap_msg = f"There's a gap between records."
    df_to_db(new_df, table_name, DBInfo.conn)
    msg = f"Insert {new_record_count} new records to table {table_name} " \
          f"by Bing Li and the time is {str(time_now)}. {overlap_msg}"
    updateRecord = LogInfo(log_time=time_now,
                           symbol=symbol,
                           start_time=start_time,
                           end_time=end_time,
                           start_id=start_id,
                           end_id=end_id,
                           new_record_count=new_record_count,
                           overlap_count=overlap_count,
                           message=msg)
    updateRecord.add_new_log(DBInfo.conn)
    print(msg)


def trade_job():
    try:
        job_detail()
    except:
        print("Getting data failed, will retry in next minute!")


if __name__ == "__main__":
    # symbol = 'BIX/USDT'
    # df = get_trade_df(symbol)
    # table_name = 'bibox_trade'
    # db_df = get_recent_records(table_name, DBInfo.conn)
    # api_ids = set(list(df['id']))
    # db_ids = set(list(db_df['id']))
    # overlap = api_ids.intersection(db_ids)
    # print(len(api_ids))
    # print(len(db_ids))
    # print(len(overlap))
    # print(overlap)
    job_detail()
