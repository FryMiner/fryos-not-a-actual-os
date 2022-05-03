import time
import sys

import os



print(r"""

███████╗██████╗░██╗░░░██╗░█████╗░░██████╗
██╔════╝██╔══██╗╚██╗░██╔╝██╔══██╗██╔════╝
█████╗░░██████╔╝░╚████╔╝░██║░░██║╚█████╗░
██╔══╝░░██╔══██╗░░╚██╔╝░░██║░░██║░╚═══██╗
██║░░░░░██║░░██║░░░██║░░░╚█████╔╝██████╔╝
╚═╝░░░░░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═════╝░
             v0.1
      
      
      Made by FryMiner   Booting up          """)



time.sleep(4)



q1=int(input("User "))
if q1==1:
    print ("Loading password stage")
    corr1=int(1)
else:
    print ("User doesnt exist")
    corr1=int(0)
    sys.exit("Error message")


time.sleep(2)











q2=int(input("password: "))
if q2==123456789:
    print ("logging in")
    corr1=int(1)
else:
    print ("WRONG")
    corr1=int(0)
    sys.exit("Error message")

time.sleep(2)


while True:
    d1a = input("Do you want to run \n A) system info B) shutdown [A/B]? : ")
    if d1a == "A":
        print(os.system("python msdosaddon.py"))
    elif d1a == "B":
        print(os.system("python msdosaddonplus.py"))

        break











