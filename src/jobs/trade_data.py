import datetime
from note.send_email import sendEmail

import ccxt
from config import DBInfo
from db_tools.write_symbol_to_db import df_to_db
from fetch_data.fetch_trades import get_trade_df
from db_tools.read_from_db import get_latest_record_from_db, get_recent_records
from jobs.utils.logUtils import LogInfo


def job_detail():
    time_now = datetime.datetime.now()
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
    last_info = get_latest_record_from_db("log_info", DBInfo.conn)
    last_trade = get_latest_record_from_db(table_name, DBInfo.conn)
    if last_trade is not None and last_info is not None:
        db_latest_id = last_trade["id"][0]
        new_df = df[df['id'] > int(db_latest_id)]
        new_record_count = len(new_df)
        db_df = get_recent_records(table_name, DBInfo.conn)
        api_ids = set(list(df['id']))
        db_ids = set(list(db_df['id']))
        overlap_ids = api_ids.intersection(db_ids)
        overlap_count = len(overlap_ids)
        last_end_id = last_info['end_id'][0]
        gap_id_count = start_id - last_end_id
        if start_id <= last_end_id:
            overlap_msg = f"Getting {overlap_count} overlap records."
        else:
            overlap_msg = f"There might be a gap of {gap_id_count} ids missing. " \
                          f"Last end id is {last_end_id} min id from API is {start_id}."
    else:
        new_df = df
        new_record_count = len(df)
        overlap_count = 0
        overlap_msg = ""
    df_to_db(new_df, table_name, DBInfo.conn)
    msg = f"Insert {new_record_count} new records to table {table_name} " \
          f"by Bing Li and the time is {str(time_now)}. {overlap_msg}"
    if overlap_count <= 0:
        sendEmail(str(time_now), msg_text=msg)
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
    job_detail()
