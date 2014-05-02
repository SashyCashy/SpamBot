'''
Created on 28-Apr-2014

@author: ReDhOoT
'''
from username_password import *                     #Import UserName and Password Entities from username_password.py File

import smtplib                                      #Import SMTP Library for email communication

from email.MIMEMultipart import MIMEMultipart       #Libraries imported for adding to,from and subject fieids in Email
from email.MIMEText import MIMEText

msg=MIMEMultipart()

msg['fromaddr']=username                             #From Field in Email
msg['toaddr']=toaddr                                 #To  Field in Email
msg['subject']='CONGRATULATIONS YOU WON !!'          #Subject Field in Email


body=text                                            #Body containing message

msg.attach(MIMEText(body,'plain'))
 #print emailAddr
server=smtplib.SMTP('smtp.gmail.com:587')             #Server Deamon to listen the client requests.  

server.starttls()

server.login(username,password)                     #Paramters passed are the username and password that were imported from username_password.py file   




from gmailcontactList import reciepents             #Import reciepents List
#print reciepents
for emailAddr in reciepents:
    print "Sending Spam to %s" %emailAddr
    server.sendmail(username,str(emailAddr),msg.as_string())    #Server sending the messages invoked by the client
    
print "Spamming Ends....."