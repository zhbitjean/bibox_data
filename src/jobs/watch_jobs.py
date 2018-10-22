import db_tools.read_from_db


def watch_mark(mark_price):
    print(f"Watch price at ${mark_price}.")
    symbol_df = db_tools.read_from_db.read_symbol_from_db()
    symbol_df = symbol_df.set_index(['date'])
    latest_time = symbol_df.index.max()
    latest_record = symbol_df.loc[latest_time, 'Close']
    last_df = symbol_df.tail(2)
    t = last_df.iloc[-1]
    r = (last_df.iloc[-1]['Close'] - last_df.iloc[0]['Close']) / last_df.iloc[-1]['Close']
    print(f"Recent price has a {r}% change.")
    if abs(r) > 0.3:
        print(f"Recent price has a {r}% change.")
    if latest_record < mark_price:
        print(f"Current close price is ${latest_record}. It's lower than watch price ${mark_price}.")
    res_dict = dict()
    res_dict['ratio'] = r
    res_dict['mark_price'] = mark_price
    res_dict['latest_price'] = latest_record
    return res_dict
