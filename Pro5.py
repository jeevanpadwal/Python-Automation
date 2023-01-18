import os
from sys import *
import shutil
from pathlib import *

def CopyDirectoryData(Old_Dirname,New_Dirname,Extention):
    
    flag = os.path.isabs(Old_Dirname)
    if flag == False:
        Old_Dirname = os.path.abspath(Old_Dirname)

    exists = os.path.isdir(Old_Dirname)

    for foldername, subfolder, Filenames in os.walk(Old_Dirname):
        os.mkdir(New_Dirname)
        
        #for subf in subfolder:
            #print("Subfolder name of "+foldername+" is "+subf)
        try:
            for fnames in Filenames:
                dest1 = New_Dirname +fnames
                

                if fnames.endswith(Extention):
                    
                    shutil.copyfile(exists,dest1)
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