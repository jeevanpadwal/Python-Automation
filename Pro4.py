
import smtplib
from email.mime.multipart import *
from email.mime.text import *
from email.mime.base import *
from email import encoders   
import psutil
from sys import *
import os
import time

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
    msg['Subject'] = "mail cheak"
    
    body = "Currently Running Process with log file"
    
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


def ProcessDisplay(Dir_Name):

    os.mkdir(Dir_Name)
    seprator = "-"*70
    Path = os.path.join(Dir_Name,"G1log.log")
    fd = open(Path,'w')
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

        print("Application name :"+argv[0])

        if(len(argv) != 3):
            print("Inavalid Arguments")
            exit()

        if(argv[1]=="-h" or argv[1]=="-H"):
            print("This application use for getting selected process running or not")
            exit()

        if(argv[1]=="-u" or argv[1]=="-U"):
            print("Usage :Application_Name Directory_Name Mail_Sendermail_ID")
            exit()

        else:
            ProcessDisplay(argv[1])
            mail_send(argv[1],argv[2])
            
        

if __name__ == "__main__":
    main()
