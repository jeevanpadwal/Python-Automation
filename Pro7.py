

import os
from sys import *
import shutil
from pathlib import *

def CopyDirectoryData(Old_Dirname,New_Dirname,Extention):

    src = Old_Dirname
    trg = os.mkdir(New_Dirname)

    files = os.listdir(src)
    try:
        for fname in files:
            #if fname.endswith(Extention):
            shutil.copy(os.path.join(src,fname),trg)

    except:
        pass

def main():
    print("arguments",len(argv))
    if(len(argv) != 4 ):
        print("Enter -h for help and -u for usage of script")
        print("Error : Insuuficent Argument")
        exit()
    
    if argv[1] == "-h" or argv[1] == "-H":
        print("This script use to copy all files of given extention to othr directory")

        exit()

    if(argv[1]=="-u" or argv[1] =="-U"):
        print("Usage : Application_Name Directory_Name Dirctory_Name_which_want_to_create")
        exit()

    else:
    
        CopyDirectoryData(argv[1],argv[2],argv[3])

if __name__ == "__main__":
    main()