import datetime
import schedule
import time

def printTest():
    now = datetime.datetime.now()
    ymd = now.strftime("%Y%m%d.%H%M%S")
    print("íėŽėę° = " + ymd)
    
if __name__ == '__main__':

    schedule.every(5).seconds.do(printTest)

    while True:
        schedule.run_pending()
        time.sleep(1)