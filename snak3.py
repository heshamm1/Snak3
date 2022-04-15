import socket
import time
import threading
import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('Snak3!', font='starwars'),
       'yellow', attrs=['bold'])
print("_______________________")
print("")
print("      By: sh1vv")
print("_______________________")
print("")

from queue import Queue
socket.setdefaulttimeout(0.25)
print_lock = threading.Lock()
target = input('Enter the host to be scanned: ')
t_IP = socket.gethostbyname(target)
print ('Starting scan on host: ', t_IP)

def portscan(port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      con = s.connect((t_IP, port))
      with print_lock:
         print(port, 'is open')
      con.close()
   except:
      pass

def threader():
   while True:
      worker = q.get()
      portscan(worker)
      q.task_done()
      
q = Queue()
#     startTime = time.time()
   
for x in range(100):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()
    
for worker in range(1, 500):
   q.put(worker)
   
q.join()
# print('Time taken:', time.time())
print("")
print("Scanning Done, good luck kidd3 :)")