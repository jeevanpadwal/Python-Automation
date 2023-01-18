
import schedule
import time
import datetime
import sys

def Task_Terminate():
    sys.exit()

def Fun():
    print("Inside Fun")

def main():
    print("Inside task scheduler")

    schedule.every(1).minutes.do(Fun)
    schedule.every(3).minutes.do(Task_Terminate)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__== "__main__":
    main()