
import psutil
from sys import *
import os
import time


def ProcessDisplay(Dir_Name):

    os.mkdir(Dir_Name)
    seprator = "-"*70
    fd = open("G1log.log",'w')
    fd.write(seprator+"\n")
    fd.write("Current Procees running at time %s"%time.asctime())
    fd.write("\n"+seprator)
    fd.write("\n")


    listprocess = []
    
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            listprocess.append(pinfo)

        except(psutil.NoSuchProcess ,psutil.AccessDenied,psutil.ZombieProcess):
            pass

        for element in listprocess:
            fd.write("%s\n" %element)
            
            

def main():
        print("__________G1's Process__________")

        print("Application name :"+argv[0])

        if(len(argv) != 2):
            print("Inavalid Arguments")
            exit()

        if(argv[1]=="-h" or argv[1]=="-H"):
            print("This application use for getting selected process running or not")
            exit()

        if(argv[1]=="-u" or argv[1]=="-U"):
            print("Usage :Application_Name Directory_Name")
            exit()

        else:
            ProcessDisplay(argv[1])
        

if __name__ == "__main__":
    main()