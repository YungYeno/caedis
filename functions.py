#! /usr/bin/env python3
import subprocess
import sys
import json
from subprocess import check_call
from colorama import init, Fore
from time import monotonic
import os

# Initialize colorama
init()

GREEN = Fore.GREEN
RED = Fore.RED
BLUE = Fore.BLUE
WHITE = Fore.WHITE


def intro():
    print(f""" {RED}
 ▄████▄      ▄▄▄         ▓█████    ▓█████▄     ██▓     ██████ 
▒██▀ ▀█     ▒████▄       ▓█   ▀    ▒██▀ ██▌   ▓██▒   ▒██    ▒ 
▒▓█    ▄    ▒██  ▀█▄     ▒███      ░██   █▌   ▒██▒   ░ ▓██▄   
▒▓▓▄ ▄██▒   ░██▄▄▄▄██    ▒▓█  ▄    ░▓█▄   ▌   ░██░     ▒   ██▒
▒ ▓███▀ ░    ▓█   ▓██▒   ░▒████▒   ░▒████▓    ░██░   ▒██████▒▒
░ ░▒ ▒  ░    ▒▒   ▓▒█░   ░░ ▒░ ░    ▒▒▓  ▒    ░▓     ▒ ▒▓▒ ▒ ░
  ░  ▒        ▒   ▒▒ ░    ░ ░  ░    ░ ▒  ▒     ▒ ░   ░ ░▒  ░ ░
░             ░   ▒         ░       ░ ░  ░     ▒ ░   ░  ░  ░  
░ ░               ░  ░      ░  ░      ░        ░           ░  
░                                   ░                 

                                        {WHITE}-- Made with ❤️  by YY""")


def nmap():
    host = sys.argv[1]
    command = str(f" nmap -sV {host}")
    result = os.system(command)
    print(f" \n {result} ")
