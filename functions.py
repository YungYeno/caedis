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
    parser.add_argument("--nmap", help="Start nmap process")
    parser.add_argument("--gobuster", help="Start gobuster dir")
    parser.add_argument("--nikto", help="Start nikto scan")
    parser.add_argument("-u", "--url", help="Target IP")
    parser.add_argument("-m", "--mode", help="Gobuster mode")
    parser.add_argument("-o", "--output", help="Output results in file")
    parser.add_argument("-w", "--wordlist", help="Path to wordlist")
    parser.add_argument("-s", "--ssl", help="Is the website secure? yes/no")
    # Initialise.
    args = parser.parse_args()

    # Assign values to variables.
    host = args.url

    # Function values to variables
    nmap = args.nmap
    gobuster = args.gobuster
    nikto = args.nikto

    # Gobuster command arguments
    mode = args.mode
    wordlist = args.wordlist
    ssl = args.ssl

    # Return all the made variables for further use
    return host, nmap, gobuster, nikto, mode, wordlist, nmap, ssl


# Nmap function to scan target for open ports.
def nmap_scan(host):
    command = str(f" nmap -sV -O {host} --script=vuln")
    result = os.system(command)
    print(f" \n {result} ")


# Gobuster function to scan target for existing directory's or subdomain.
def gobuster_scan(host, wordlist, mode, ssl):
    if ssl == "yes" or ssl == "y":
        command = str(f" gobuster {mode} -u https://{host}/ -w {wordlist}")
    else:
        command = str(f" gobuster {mode} -u http://{host}/ -w {wordlist}")
    result = os.system(command)
    print(f"\n {result}")


def nikto_scan(host):
    command = str(f" nikto -h {host}")
    result = os.system(command)
    print(f"\n {result}")

# TODO: ZORG ERVOOR DAT APARTR FUNCTIES KUNNEN WORDEN GESTART DOOR DE GEBRUIKER!! (python3 caedis.py --nmap --gobuster --nikto -u 1.1.1.1 -s yes -w /path/to/wordlist)
