import random
import string
import time
import pystyle
from pystyle import *
import colorama
from colorama import *

System.Size(170, 47)

def gen():
    characters = string.ascii_lowercase + string.digits
    for i in range(99999999999999999999999999999):
        # print(Fore.RED + "https://discord.gg/%s\n" .join(random.sample(characters, 32)))
        print(
            Fore.RED + ">[ ] https://discord.gift/%s  " % "".join(random.sample(characters, 16)))
        time.sleep(0.025)
    input()

banner1 = """


         ▄▀▀▄    ▄▀▀▄  ▄▀▀▄▀▀▀▄      ▄▀▀█▄▄   ▄▀▀█▀▄   ▄▀▀▀▀▄  ▄▀▄▄▄▄   ▄▀▀▀▀▄   ▄▀▀▄▀▀▀▄  ▄▀▀█▄▄       ▄▀▀▀▀▄   ▄▀▀█▄▄▄▄  ▄▀▀▄ ▀▄ 
        █   █    ▐  █ █   █   █     █ ▄▀   █ █   █  █ █ █   ▐ █ █    ▌ █      █ █   █   █ █ ▄▀   █     █        ▐  ▄▀   ▐ █  █ █ █ 
        ▐  █        █ ▐  █▀▀▀▀      ▐ █    █ ▐   █  ▐    ▀▄   ▐ █      █      █ ▐  █▀▀█▀  ▐ █    █     █    ▀▄▄   █▄▄▄▄▄  ▐  █  ▀█ 
          █   ▄    █     █            █    █     █    ▀▄   █    █      ▀▄    ▄▀  ▄▀    █    █    █     █     █ █  █    ▌    █   █  
           ▀▄▀ ▀▄ ▄▀   ▄▀            ▄▀▄▄▄▄▀  ▄▀▀▀▀▀▄  █▀▀▀    ▄▀▄▄▄▄▀   ▀▀▀▀   █     █    ▄▀▄▄▄▄▀     ▐▀▄▄▄▄▀ ▐ ▄▀▄▄▄▄   ▄▀   █   
                 ▀    █             █     ▐  █       █ ▐      █     ▐           ▐     ▐   █     ▐      ▐         █    ▐   █    ▐   
                      ▐             ▐        ▐       ▐        ▐                           ▐                      ▐        ▐        

"""


print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(banner1 + '\n\n')))

#Write.Print("[!] a lot of link will be generate but the only good one will be write in green there is aproximatively one gren for 10 000 red just wait for the green one !", Colors.blue_to_red, interval=0.001)
#print()
Write.Input("[?] enter to start generation", Colors.blue_to_red, interval=0.001)
print()
print()
print()
gen()
