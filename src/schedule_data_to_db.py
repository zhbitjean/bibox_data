import schedule
import time
import datetime
from db_tools.write_symbol_to_db import write_symbol_to_db
import ccxt
from voceanemail.send_email import sendEmail

time_now = datetime.datetime.utcnow()


def job():
    try:
        write_symbol_to_db()
        print("Insert date to db by Bing Li and the time is " + str(time_now))
    # return sendEmail(time_now)
    except ccxt.base.errors.RequestTimeout:
        print("Getting data failed, will retry in next minute!")


schedule.every().minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)

print("start running...")

while 1:
    schedule.run_pending()
    time.sleep(1)
