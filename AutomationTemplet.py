from sys import *
from os import *

def Script_Task(No):   
    if(No % 2 == 0):
        print("It is even number")
    else :
        print("it is odd number") 


def main():
    print("___________Jeevan's Script_____________")

    print("Automation scrip started with name :",argv[0])
    
    if(len(argv) != 2):
        print("Use -h for the help and use -u for usage of the script")
        print("Error :Insufficient arguments")
        exit()

    if(argv[1] == "-h" or argv[1] == "-H"):
        print("Help : This scrip is used to perform __________")
        exit()

    if((argv[1]== "-u") or (argv[1] =="-U")):
        print("Usage : Provide ____ Numbner of arguments as")
        print("First argument as :____")
        print("Second argument as :________")
        exit()
    
    else:
        Script_Task(int(argv[1]))
        
if __name__ =="__main__":
    main()