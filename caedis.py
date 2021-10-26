from functions import *

if __name__ == '__main__':
    intro()
    host, nmap, gobuster, nikto, mode, output, wordlist, ssl = arguments()
    if nmap == "y" or nmap == "yes":
        nmap_scan(host)
    if gobuster == "y" or gobuster == "yes":
        gobuster_scan(host, wordlist, mode, ssl)
    if nikto == "y" or nmap == "yes":
        nikto_scan(host)

