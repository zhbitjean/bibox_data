import schedule
import time
from jobs.watch_jobs import watch_mark

schedule.every().minutes.do(watch_mark, 0.35)

print("start running...")

while 1:
    schedule.run_pending()
    time.sleep(1)

