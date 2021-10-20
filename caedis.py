from functions import *

if __name__ == '__main__':
    intro()
    host, mode, output, wordlist, ssl = arguments()
    nmap(host)
    dirb(host, wordlist, mode, ssl)
