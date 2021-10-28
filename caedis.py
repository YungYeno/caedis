from functions import *

if __name__ == '__main__':
    intro()
    host, nmap, gobuster, nikto, mode, output, wordlist, ssl = arguments()
    if nmap is True:
        nmap_scan(host)
    if gobuster is True:
        gobuster_scan(host, wordlist, mode, ssl)
    if nikto is True:
        nikto_scan(host)

