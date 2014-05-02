'''
Created on 01-May-2014

@author: ReDhOoT
'''
    
pattern='[A-Za-z_0-9]+@gmail\.com'

import gdata.contacts.service       #Import libraries form Gdata
import re                           #Import libraries for Regular Expression
from username_password import *     #Import UserName and Password Entities from username_password.py File

client=gdata.contacts.service.ContactsService()     #Invoke ContactsService Method

client.ClientLogin('sashpre001@gmail.com',password)               #Login to the Gmail Account using username and Password imported from username_password.py file

email_feed=client.GetContactsFeed()             
address=re.compile(pattern)                         #Extracting only Gmail Accounts, checking for pattern

reciepents=[]
while(email_feed):      
    for user in email_feed.entry:               #Extracting data from Entry Object
        #print user.title.text
        
        #print address
    
        for email in user.email:                #Extracting Mail Address from User Object    
            #print "2.."
            #print email.address
            if address.match(email.address):    #Checking for 'gmail' pattern
                #print "1.."
                print email.address             #Print the email(gmail) Address
                reciepents.append(email.address)
           
        
        ret=email_feed.GetNextLink() #if(ret):    #Go to the next Feed
        #print ret
#else ret
    
        
    if ret is not None:
        #print ret.href  
        email_feed=client.GetContactsFeed(ret.href)
    else:
        break
  
    
    