import os
import sys
import pyfiglet
from urllib.request import *
from urllib.error import *

os.system(chr(27)+"[36m")

os.system("clear")

banner = pyfiglet.figlet_format("TORAPF",font="standard")
print(banner)

print("   Author : Rahat Khan Tusar(RKT)")
print("  Github : https://github.com/r3k4t")

print

#Open links file

file = open('link.txt','r')
link = input('Enter The Website Link(www.site.com) : ')

for i in range(10000000000000000000000):
   sub_link = file.readline().split('\n')[0]
   if not sub_link:
      break
   req_link ='http://'+link+'/'+sub_link
   try:
      response =urlopen(req_link)
   except HTTPError as e:
      continue
   except URLError as e:
      continue
   else:
      print(" ==[TOR-NETWORK]==> ",req_link)