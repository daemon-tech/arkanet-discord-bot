import os
from time import sleep

def reboot_on_timer():
    os.system("python3 arkanet.py")
    
if __name__ == "__main__":
    sleep(1)
    reboot_on_timer()