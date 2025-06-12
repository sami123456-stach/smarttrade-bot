import schedule
import time
from bot import send_signal

def job():
    send_signal()

schedule.every().day.at("17:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
