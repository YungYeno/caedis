from functions import *

if __name__ == '__main__':
    intro()
    host, nmap, gobuster, nikto, mode, output, wordlist, ssl = arguments()
    if nmap:
        nmap_scan(host)
    if gobuster:
        gobuster_scan(host, wordlist, mode, ssl)
    if nikto:
        nikto_scan(host)

