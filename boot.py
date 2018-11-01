#One time setup when device boots 
import main 
import json
import os
from setup import setup
#setup() #This is needed if the libraries below are not installed
import requests
import urllib.request

tank_id_file = "tank_id"

#requests google to create a new tank_id 
def get_tank_from_google():
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.post("http://iglooboiler.appspot.com/tank", data=payload)
    tank_id = r.text
    return tank_id

#Returns tank_id from tank_id_file
def get_tank_from_file():
    if not os.path.isfile(tank_id_file):
        tank_id = ""
    else:
        with open(tank_id_file, "r") as myfile:
            tank_id = myfile.read()
            tank_id = tank_id.split("\n")[0]
    
    return tank_id

#Gets ID from file if available, otherwise creates new ID by requesting google
def get_tank_id():
    tank_id = get_tank_from_file()
    if tank_id ==  "": 
        tank_id = get_tank_from_google()
        with open(tank_id_file, "w+") as writer:
            writer.write(str(tank_id) + "\n")
    return tank_id

def run():
    tank_id = get_tank_id()
    main.main(tank_id) 

if __name__ == "__main__": run()