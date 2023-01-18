import os
import psutil
from sys import *
import os


def ProcessDisplay(Pro_Name):

    listprocess = []
    
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            listprocess.append(pinfo)

        except(psutil.NoSuchProcess ,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    for element in listprocess:
        if element['name'] == Pro_Name:
            print("Process is running :")
            print(element)

def main():
    

        print("Application name :"+argv[0])

        if(len(argv) != 2):
            print("Inavalid Arguments")
            exit()

        if(argv[1]=="-h" or argv[1]=="-H"):
            print("This application use for getting selected process running or not")
            exit()

        if(argv[1]=="-u" or argv[1]=="-U"):
            print("Usage :Application_Name Process_Name")
            exit()

        try:
            ProcessDisplay(argv[1])
        except ValueError:
            print("Error : Invalid datatype of input")
        except Exception:
            print("Error : Invalid Input")

if __name__ == "__main__":
    main()