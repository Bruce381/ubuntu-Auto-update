"""
made by <Bruce> at May 3 2024
it will update the ubuntu system
"""

import time
import subprocess

password = input('Your pass word: ')

while True:
    try :
        subprocess.run(["sudo","-S","apt","update"],input=password, text=True)
        time.sleep(2)
        subprocess.run(["sudo","-S","apt","upgrade","-y"],input=password, text=True)
        time.sleep(2)
        subprocess.run(["sudo","-S","apt","autoremove","-y"],input=password, text=True)
        print("sleep...")
        time.sleep(604800)  #change the number to change how long it will check
        print("update checking...")
    except :
        print("Something went wrong")
        break

