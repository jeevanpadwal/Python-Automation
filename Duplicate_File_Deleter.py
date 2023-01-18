from tkinter.filedialog import askdirectory

from tkinter import Tk
from sys import *  
import time
import os
import hashlib
from pathlib import *
import smtplib
from email.mime.multipart import *
from email.mime.text import *
from email.mime.base import *
from email import encoders   
import psutil
from sys import *



def mail_send(Dir_Name,Sender_Mail):

    flage = os.path.isabs(Dir_Name)

    if flage == False:
        path = os.path.abspath(Dir_Name)

    Files = []

    for folder, dir,file in os.walk(Dir_Name):
        for f in file:
            Files.append(f)
    
    fromaddr = "supercoin2002@gmail.com"
    toaddr = Sender_Mail
    
    msg = MIMEMultipart()
    
    msg['From'] = fromaddr
    
    msg['To'] = toaddr
    msg['Subject'] = "Douplicate File Names In selected Folder"
    
    body = "Dear,\n Sir Please Cheak the attachment which contains douplicate file names of selected folder \n if you select yes in your applicatin then this files get deleted if select not then don't delete\n Thank You\n"
    
    msg.attach(MIMEText(body, 'plain'))

    for i in Files:

        file_path = os.path.join(Dir_Name,f)
        
        attachment = open(file_path, "rb")
          
        p = MIMEBase('application', 'octet-stream')
            
        p.set_payload((attachment).read())
                
        encoders.encode_base64(p)
                
        p.add_header('Content-Disposition', "attachment; filename= %s" % f)
                
        msg.attach(p)
  
    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()
                
    s.login(fromaddr, "qvbitgkjtejhifdt")
                
    text = msg.as_string()

    s.sendmail(fromaddr, toaddr, text)

    s.quit()
    print("Mail send")



def PrintDublicate(Dir_Name,log_dir ="Duplicate"):

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass


    Duplicate_File_Counter = 1

    seprator = "-" * 80
    file_path = Dir_Name
    log_path = os.path.join(log_dir,"Log.txt")
    fd = open(log_path,'w')
    
    list_of_files = os.walk(file_path)

    fd.write(" Dublicate File Names in this "+Dir_Name+" Folder"+"\n")
    fd.write(seprator + "\n")
    
    unique_files = dict()
    
    for root, folders, files in list_of_files:

        for file in files:
    
    
            file_path = Path(os.path.join(root, file))
    
            
            Hash_file = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
    
            if Hash_file not in unique_files:
                unique_files[Hash_file] = file_path
            
            else:
                
                fd.write("%s""] "%Duplicate_File_Counter+"%s"%file_path+"\n")
                
                Duplicate_File_Counter = Duplicate_File_Counter + 1
    
    return log_dir
  

def RemoveDublicate(Dir_Name):

    file_path = Dir_Name
    list_of_files = os.walk(file_path)
    
    unique_files = dict()
    
    for root, folders, files in list_of_files:

        for file in files:
    
    
            file_path = Path(os.path.join(root, file))
    
            Hash_file = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
    
            if Hash_file not in unique_files:
                unique_files[Hash_file] = file_path
            
    
            else:
                
                
                os.remove(file_path)
                

def main():
    

    if(len(argv) != 2):
        print("use -h for the help or -u for the usage of the script ")
        print("Error :Invalid arguments")
        exit()

    if(argv[1] == "-h" or argv[1] == "-H"):
        print("This scrip used for thr the finding dublicate files from folder")
        exit()

    if(argv[1] == "-u" or argv[1] == "-U"):
        print("Usage :Application_Name Folder_Name")
        exit()

    else:
        Tk().withdraw()
        file_path = askdirectory(title="Select a folder")

        log_dir = PrintDublicate(file_path)

        mail_send(log_dir,argv[1])
        print("-------------------------------------------------------------------------------------------------")
        print("Please Cheak Your Email And Cheak Doublicate File Names Attached to the Mail\n")
        print("-------------------------------------------------------------------------------------------------")

        print("Enter Yes : To delete Douplicate Files")
        print("Enter No : To Not Delete Douplicate Files")
        
        desion = input()

        if desion.lower() =="yes":
            RemoveDublicate(file_path)
            print("Douplicate files Deleted")

        elif desion.lower() == "no":
             exit()
        

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()

    result = end_time - start_time
    print("Time require for execution :",result)
