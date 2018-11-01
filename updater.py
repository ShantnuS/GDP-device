#Updates the OS of the raspberry Pi 
import os
import time 

def update():
    #time.sleep(600)
    os.system("git pull origin live")
    os.system("sudo reboot")
    

update()