#One time setup when device boots 
import main 
import urllib.request
import json
import os

tank_id_file = "tank_id.txt"

def get_tank_from_google():
    item  = json.load(urllib.request.urlopen('http://iglooboiler.appspot.com/tank'))
    tank_id = item[0]['id']
    print("GOT ID FROm google")
    return tank_id

def get_tank_from_file():
    if not os.path.isfile(tank_id_file):
        tank_id = ""
    else:
        with open(tank_id_file, "r") as myfile:
            tank_id = myfile.read()
            tank_id = tank_id.split("\n")[0]
    
    return tank_id

def get_tank_id():
    tank_id = get_tank_from_file()
    if tank_id ==  "": 
        tank_id = get_tank_from_google()
        with open(tank_id_file, "a") as writer:
            writer.write(str(tank_id) + "\n")
    return tank_id

def run():
    tank_id = get_tank_id()
    print(tank_id)
    main.main(tank_id) 

if __name__ == "__main__": run()