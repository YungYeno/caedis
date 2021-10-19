from functions import *

if __name__ == '__main__':
    intro()
    host, mode, output, wordlist = arguments()
    nmap(host)
    dirb(host, wordlist, mode)
