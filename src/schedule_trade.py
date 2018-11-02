import time

import schedule

from jobs.trade_data import trade_job

schedule.every(10).minutes.do(trade_job)

print("Start downloading trade data from Bibox API ...")

while 1:
    schedule.run_pending()
    time.sleep(1)
