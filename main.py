import random
import string
import time
import pystyle
from pystyle import *
import colorama
from colorama import *

System.Size(170, 47)

def nitro():
    caracteres =  ['a', 'b', 'c', 'd', 'e', 'F','g','h','i','j','k','l','m','n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x','y','z','0','1','2', '3','4', '5','6','7','8','9']

    while True:
        nitrocode = ""
        for i in range(16):
            nitrocode = f"{nitrocode}{random.choice(caracteres)}"
        print(
            Fore.RED + F"https://discord.gift/{nitrocode}")
        time.sleep(0.025)
        with open("nitros. txt", "a+") as nitroFile:
            nitroFile.write(f"https://discord.gift/{nitrocode}\n")

            nitroFile.close

def gen():
    characters = string.ascii_lowercase + string.digits
    for i in range(99999999999999999999999999999):
        print(
            Fore.RED + ">[ ] https://discord.gift/%s  " % "".join(random.sample(characters, 16)))
        with open('nitro.txt', 'a+') as file: file.write("df")
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
Write.Input("[?] enter to start generation", Colors.blue_to_red, interval=0.001)
print()
print()
print()

nitro()
