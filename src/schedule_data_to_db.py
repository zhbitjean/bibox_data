import time

import schedule

from jobs.fetch_symbol_data import job


schedule.every().minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)

print("start running...")

while 1:
    schedule.run_pending()
    time.sleep(1)

