#!/usr/bin/env python3

import urllib.request, asyncio, socket, os

def get(which):
    if which == 'current':
        with open("/home/satch/scripts.d/ip-address-tracking/public.txt","r") as file:
            if file.mode == "r":
                current = file.read().strip()
                file.close()
                return current
    elif which == 'new':
        new = urllib.request.urlopen('http://ip.42.pl/raw').read().decode('utf8')
        return new
    else:
        print("Please specify if you want new or current ip address")
        return

def set(ip):
    if is_valid(ip) == True:
        with open("/home/satch/scripts.d/ip-address-tracking/public.txt","w") as file:
            if file.mode == "w":
                file.write(ip + os.linesep)
                file.close()
                return
    else:
        print("Not a valid ip")

def is_valid(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False





def compare(a, b):
    return a == b

def has_changed():
    if compare(get('new'), get('current')) != True:
        return True
    else:
        return False
