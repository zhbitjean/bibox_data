import schedule
import time
import datetime
from jobs.watch_jobs import watch_mark
from jobs.fetch_symbol_data import job
from voceanemail.send_email import sendEmail
import logging

schedule.every().minutes.do(watch_mark, 0.35)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)

print("start running...")

while 1:
    schedule.run_pending()
    time.sleep(1)

# if __name__ == "__main__":
#     watch_mark(0.35)V
