#!/usr/bin/python3
import click
import datetime
import pyfiglet
from pyfiglet import Figlet
import time
import progressbar
from colorama import Fore,init
from pathlib import Path


from vTest.Function import DOS, scan,DHCPspoofing,DNSspoofing,ARPspoofing,MACflooder,IPspoofing,Sniffing,MITMs,ICMPredirection,ReverseShell,SessionHijacking,SessionReset,DOS,DOS_Memory


# Print name of Tools using pyfiglet 
print(Fore.GREEN  + '\n')
f = Figlet(font='standard')
init(autoreset=True)
print(f.renderText("   v - T e  s  t  "))

print('    v2.2')
init(autoreset=True)
print(Fore.BLUE + '    https://github.com/Ensaodocker ')
print('   ',Fore.GREEN  + str(datetime.datetime.now()))
print('\n')




# Print Progress Bar :
def animated_marker(x):
    widgets = [Fore.GREEN + 'Loading :  ', progressbar.AnimatedMarker()]
    init(autoreset=True)
    bar = progressbar.ProgressBar(widgets=widgets).start()
    for i in range(x):
        time.sleep(0.1)
        bar.update(i)       
# Driver's code
animated_marker(10)
print('\n')


# For Option : using click library 
@click.command()
@click.option("--name", prompt=Fore.GREEN  + """[+] Please enter attack number : 
                 \n\t1  - scan 
                 \n\t2  - DNSspoofing 
                 \n\t3  - ARPspoofing 
                 \n\t4  - IPspoofing 
                 \n\t5  - Sniffing 
                 \n\t6  - ICMPredirection 
                 \n\t7  - ReverseShell 
                 \n\t8  - SessionHijacking 
                 \n\t9  - SessionReset 
                 \n\t10 - DOS 
                 \n\t11 - DOSmemory
                 \n\n --> Attack  """

, help="""Provide your attacks number : \t\n
                 1  - scan  \n
                 2  - DNSspoofing \n
                 3  - ARPspoofing \n
                 4  - IPspoofing \n
                 5  - Sniffing \n
                 6  - ICMPredirection \n 
                 7  - ReverseShell \n
                 8  - SessionHijacking \n
                 9  - SessionReset \n
                 10 - DOS \n
                 11 - DOSmemory 
          """)



#main function
def main(name):
    print('')
    time.sleep(0.4)


    if name == '1' :
        scan()

    elif name == '2' :
        DNSspoofing()

    elif name == '3' :
        ARPspoofing()

    elif name == '4' :
        IPspoofing()

    elif name == '5' :
        Sniffing()

    elif name == '6' :
        ICMPredirection()

    elif name == '7' :
        ReverseShell()

    elif name == '8' :
        SessionHijacking()

    elif name == '9' :
        SessionReset()

    elif name == '10' :
        DOS()

    elif name == '11' :
        DOS_Memory()


    else : 
        print('\nPlease enter a Correct number attack , Show help for more details ( --help )')



