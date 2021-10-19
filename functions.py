#! /usr/bin/env python3
from colorama import init, Fore
import os
import argparse

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


def arguments():
    # The arguments for Caedis.
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="Target IP")
    parser.add_argument("-m", "--mode", help="Gobuster mode")
    parser.add_argument("-o", "--output", help="Output results in file")
    parser.add_argument("-w", "--wordlist", help="Path to wordlist")
    # Initialise.
    args = parser.parse_args()

    # Assign values to variables.
    host = args.url
    mode = args.mode
    output = args.output
    wordlist = args.wordlist

    return host, mode, output, wordlist


# Nmap function to scan target for open ports.
def nmap(host):
    command = str(f" nmap -sV {host}")
    result = os.system(command)
    print(f" \n {result} ")


# Gobuster function to scan target for existing directory's or subdomain.
def dirb(host, wordlist, mode):
    command = str(f" gobuster {mode} -u https://{host}/ -w {wordlist}")
    result = os.system(command)
    print(f"\n {result}")
