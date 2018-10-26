import datetime
import logging

import ccxt

from db_tools.write_symbol_to_db import write_symbol_to_db
from info_from_site.bibox_symbols import get_symbol_df


def job():
    time_now = datetime.datetime.utcnow()
    try:
        df = get_symbol_df()
        write_symbol_to_db(df)
        print(f"get dat {df}")
        print("Insert date to db by Bing Li and the time is " + str(time_now))
        # logging.info(f"get dat {df}")
        # logging.info("Insert date to db by Bing Li and the time is " + str(time_now))
    except ccxt.base.errors.RequestTimeout:
        print("Getting data failed, will retry in next minute!")


if __name__ == "__main__":
    job()
