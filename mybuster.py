#!/usr/bin/python

import sys
import os
import requests
from colorama import Fore

print(Fore.LIGHTGREEN_EX + '''

 ███▄ ▄███▓▓██   ██▓ ▄▄▄▄    █    ██   ██████ ▄▄▄█████▓▓█████  ██▀███  
▓██▒▀█▀ ██▒ ▒██  ██▒▓█████▄  ██  ▓██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
▓██    ▓██░  ▒██ ██░▒██▒ ▄██▓██  ▒██░░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
▒██    ▒██   ░ ▐██▓░▒██░█▀  ▓▓█  ░██░  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  
▒██▒   ░██▒  ░ ██▒▓░░▓█  ▀█▓▒▒█████▓ ▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
░ ▒░   ░  ░   ██▒▒▒ ░▒▓███▀▒░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
░  ░      ░ ▓██ ░▒░ ▒░▒   ░ ░░▒░ ░ ░ ░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░
░      ░    ▒ ▒ ░░   ░    ░  ░░░ ░ ░ ░  ░  ░    ░         ░     ░░   ░ 
       ░    ░ ░      ░         ░           ░              ░  ░   ░     
            ░ ░           ░                                            

''')
print("[+] By th3g3ntl3m4n [+]")

if len(sys.argv) != 3:
    print(Fore.LIGHTBLUE_EX)
    print("Usage: python3 mybuster.py endpoint_wl.txt url")
    print("Example: python3 endpoints.txt http://example.com:8000")
    print("endpoint wordlist has to be /directory/file.extension")
    exit()

print(Fore.RESET)
wordlist = open(sys.argv[1],'r')
url = sys.argv[2]

lines = wordlist.readlines()

count = 0
for line in lines:
    count += 1
    endpoint = line.strip()
    
    status_code = requests.get(url + endpoint).status_code
    if status_code == 200:
        print(url + endpoint + " --> " + Fore.GREEN + "[Status: " + str(status_code) + "]" + Fore.RESET)
    
    if status_code == 301:
        print(url + endpoint + " --> " + Fore.GREEN + "[Status: " + str(status_code) + "]" + Fore.RESET)
    
    if status_code == 302:
        print(url + endpoint + " --> " + Fore.GREEN + "[Status: " + str(status_code) + "]" + Fore.RESET)
    
    #if status_code == 403:
        #print(url + endpoint + " --> " + Fore.RED + "[Status: " + str(status_code) + "]" + Fore.RESET)
