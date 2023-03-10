
import schedule 
import time
import datetime
import sys

def Task_Terminat():
    sys.exit()

def Task_Minute():
    print("Task based on minutes gets schedule at :",datetime.datetime.now())

def Tas_Hour():
    print("Task based on hour gets schedule at :",datetime.datetime.now())
    
def Task_Day():
    print("Task based on Day gets schedule at :",datetime.datetime.now())

def main():
    print("Inside task scheduler")
    print("Current time :",datetime.datetime.now())
   
    schedule.every(1).minutes.do(Task_Minute)
    schedule.every(1).hour.do(Task_Day)
    schedule.every(1).day.do(Task_Day)
    schedule.every().saturday.at("18:00").do(Task_Day)
    #schedule.every().sunday.at("05:00").do(Task_Terminat)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__== "__main__":
    main()
