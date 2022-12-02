#This is going to be a living document 
#Import all needed librarys
import pyfiglet
import sys
import socket
import re
import threading
from datetime import datetime
from queue import Queue
import time 
#################################################################################################################################

#Make the banner using pyfiglet
ascii_banner = pyfiglet.figlet_format("Mac's Port Scanner")
print(ascii_banner)

#Ask for user input of target or target range 
ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
if ip_add_pattern.search(ip_add_entered):
    print(f"{ip_add_entered} is a valid ip address")

#progress banner
print('_' * 50)
print('Scanning Target:' + ip_add_entered)
start = datetime.now()
print('Scanning started at:' + str(datetime.now()))
print('_' * 50)

try:
     
    # will scan ports between 1 to 1001
    for port in range(1,500):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
         
        # returns an error indicator
        result = s.connect_ex((ip_add_entered,port))
        if result ==0:
            print("Port {} is open".format(port))
        s.close()

         
except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
except socket.error:
        print("\ Server not responding !!!!")
        sys.exit()
end = datetime.now()
print('Total time elapsed:' , end - start)
#################################################################