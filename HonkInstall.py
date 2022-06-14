from urllib.request import urlretrieve
import sys
from time import sleep
from webbrowser import open as webopen
from os import system, startfile, remove as rm
import socket
from colorama import Fore, init
init(autoreset=True)

#Progress Bar And Size Reporter
def reporter(blocknum, blocksize, totalsize):
    readsofar = blocknum * blocksize
    if totalsize > 0:
        percent = readsofar * 1e2 / totalsize
        s = "\r%5.1f%% %*d out of %d" % (
            percent, len(str(totalsize)), readsofar, totalsize)
        sys.stderr.write(s)
        if readsofar >= totalsize:
            sys.stderr.write("\n")
    else:
        sys.stderr.write("read %d\n" % (readsofar,))

#UrlRetriever
def powpow(name, repname, replink):
    print("Installing + name + "...")
    urlretrieve(replink, repname, reporter)
    startfile(repname)
    sleep(3)
    rm(repname)
    print(name + " Installed!")
    exit(sleep(3))

#Check Is Internet Connection
def is_connected():
  try:
    host = socket.gethostbyname("github.com")
    s = socket.create_connection((host, 80), 2)
    return 'Yes'
  except:
     pass
  return 'No'

#Main
system('cls')
print(Fore.RED +"[S>] Testing Internet...")
if is_connected() == 'Yes':
    system('cls')
    print(Fore.RED +"[S>] Internet is connected")
    print(" ")
    print(Fore.WHITE +"Welcome, This small Python script will install selected GooseMod version for you!")
    print(Fore.WHITE + "All credits to GooseNest Team")
    print(Fore.RED + "THIS SCRIPT MUST BE RUN AS ADMINISTRATOR!!!")
    print(Fore.BLUE + "1. OpenAsar For Discord Stable")
    print(Fore.BLUE + "2. OpenAsar For Discord PTB")
    print(Fore.BLUE + "3. OpenAsar For Discord Canary")
    print(Fore.BLUE + "4. GooseMod For Discord Stable")
    print(Fore.BLUE + "5. GooseMod For Discord Public Test Build (PTB)")
    print(Fore.BLUE + "6. GooseMod For Discord Canary")
    print(Fore.BLUE + "7. GooseMod For Discord Developer (NOT Canary)")
    print(Fore.BLUE + "8. GooseMod For Discord Web")
    print(Fore.BLUE + "99. Exit")
    gosever = input("(0/1/2/3/4/5)")
    print(" ")
    
    if gosever == '1':
        powpow('OpenAsar Discord Stable', 'OADS.bat', 'https://github.com/xemulat/MyFilesForDDL/releases/download/openasar/openasarstable.bat')

    if gosever == '2':
        powpow('OpenAsar Discord Stable', 'OADP.bat', 'https://github.com/xemulat/MyFilesForDDL/releases/download/openasar/openasarptb.bat')

    if gosever == '3':
        powpow('OpenAsar Discord Canary', 'OADC.bat', 'https://github.com/xemulat/MyFilesForDDL/releases/download/openasar/openasarcanary.bat')

    if gosever == '4':
        powpow('GooseMod Discord Stable', 'GMDS.bat', 'https://github.com/xemulat/MyFilesForDDL/releases/download/goosemod/goosemodstable.bat')

    if gosever == '5':
        powpow('GooseMod Discord PTB', 'GMDP.bat', 'https://github.com/xemulat/MyFilesForDDL/releases/download/goosemod/goosemodptb.bat')

    if gosever == '6':
        powpow('GooseMod Discord Canary', 'GMDC.bat', 'https://github.com/xemulat/MyFilesForDDL/releases/download/goosemod/goosemodcanary.bat')

    if gosever == '7':
        powpow('GooseMod Discord Development', 'GMDD.bat', 'https://github.com/xemulat/MyFilesForDDL/releases/download/goosemod/goosemoddev.bat')

    if gosever == '8':
        webopen('https://chrome.google.com/webstore/detail/goosemod-for-web/clgkdcccmbjmjdbdgcigpocfkkjeaeld')
        print("GooseMod For Discord Web URL Opened!")
        exit(sleep(3))
        
        if gosever == '99':
            exit(sleep(2))
