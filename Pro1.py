import os
import psutil
from sys import *
import os


def ProcessDisplay():

    listprocess = []
    
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            listprocess.append(pinfo)

        except(psutil.NoSuchProcess ,psutil.AccessDenied,psutil.ZombieProcess):
            pass

        for element in listprocess:
            print(element)

def main():
        print("__________G1's Process__________")

        print("Application name :"+argv[0])

        try:
            ProcessDisplay()
        except ValueError:
            print("Error : Invalid datatype of input")
        except Exception:
            print("Error : Invalid Input")

if __name__ == "__main__":
    main()