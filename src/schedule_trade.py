import time

import schedule

from jobs.trade_data import trade_job

schedule.every(15).minutes.do(trade_job)

print("start trade data...")

while 1:
    schedule.run_pending()
    time.sleep(1)
