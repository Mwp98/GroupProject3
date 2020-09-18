import requests
import os.path
from os import path
list = []
Z = 0
K = 0

if path.isfile('http_access_log.txt') == False:
  url='https://s3.amazonaws.com/tcmg476/http_access_log'
  r = requests.get(url, allow_redirects=True)
  open ('http_access_log.txt','wb').write(r.content)
  print('downloading file')


else:
 print ('File Log has already been downloaded')
 
  
logfile = open('http_access_log.txt', 'r')

print("The total number of requests made in the last year were")
with open('http_access_log.txt') as j:
    
    for line in j:
        V = line.split(' ')
        list.append(V[3])
        
    for date in list:
         if (date[10:12] == '95'):
           K = K + 1;
    
print(K) 

print("The total requests made in the time period were")
with open('http_access_log.txt') as j:
    
    for line in j:
        V = line.split(' ')
        list.append(V[3])
        Z = Z + 1;

print (Z)
