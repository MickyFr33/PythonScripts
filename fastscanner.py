import pyfiglet
import sys
import socket
import os
import subprocess, signal, time 
import re
import threading
from datetime import datetime
from queue import Queue
#################################################################################################################################

#Make the banner using pyfiglet
my_banner = pyfiglet.figlet_format("Mac's Port Scanner")
print(my_banner)
#Ask for user input of target or target range 
ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
if ip_add_pattern.search(ip_add_entered):
    print(f"{ip_add_entered} is a valid ip address")

#progress banner
print('_' * 50)
print('Scanning Target:' + ip_add_entered)
t1 = datetime.now()
print('Scanning started at:' + str(datetime.now()))
print('_' * 50)

# Main Function
def main():
    socket.setdefaulttimeout(0.30)
print_lock = threading.Lock()
discovered_ports = []

def portscan(port):

       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       
       try:
          portx = s.connect((ip_add_entered, port))
          with print_lock:
             print("Port {} is open".format(port))
             discovered_ports.append(str(port))
          portx.close()

       except (ConnectionRefusedError, AttributeError, OSError, KeyboardInterrupt):
          pass

def threader():
       while True:
          worker = q.get()
          portscan(worker)
          q.task_done()
      
q = Queue()
     
    #startTime = time.time()
     
for x in range(200):
       t = threading.Thread(target = threader)
       t.daemon = True
       t.start()

for worker in range(1, 65536):
       q.put(worker)

q.join()

t2 = datetime.now()
total = t2 - t1
print("Port scan completed in "+str(total))
print("-" * 60)
print("Mac recommends the following Nmap scan:")
print("*" * 60)
print("nmap -p{ports} -sV -sC -T4 -Pn -oA {ip} {ip}".format(ports=",".join(discovered_ports), ip=ip_add_entered))
print("*" * 60)
nmap = "nmap -p{ports} -sV -sC -T4 -Pn -oA {ip} {ip}".format(ports=",".join(discovered_ports), ip=ip_add_entered)
t3 = datetime.now()
total1 = t3 - t1