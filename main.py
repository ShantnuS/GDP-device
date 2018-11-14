#Main script for reading and trasmitting temperatures 
import time
import json
import logging 
import os
import urllib.request
from ds18b20 import DS18B20

def read_sensor1(ds_object):
    return ds_object.tempC(0)

def read_sensor2(ds_object):
    return ds_object.tempC(1)

def read_sensor3(ds_object):
    return ds_object.tempC(2)

def transmit(tank_id, sensor1, sensor2, sensor3):
    body = {'tankId': tank_id, 'sensor1': sensor1, 'sensor2': sensor2, 'sensor3': sensor3}
    logging.info(str(body))
    myurl = "http://iglooboiler.appspot.com/readings"
    req = urllib.request.Request(myurl)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')
    req.add_header('Content-Length', len(jsondataasbytes))
    response = urllib.request.urlopen(req, jsondataasbytes)
    return response

def get_test():
    item  = json.load(urllib.request.urlopen('http://iglooboiler.appspot.com/readings'))
    return item

def main(tank_id):
    logging.basicConfig(filename='main.log', format="%(asctime)s %(levelname)s: %(message)s",level=logging.DEBUG)   
    ds_object = DS18B20()

    while True:
        #Read sensors
        #os.system('modprobe w1-gpio')
        #os.system('modprobe w1-therm')
        sensor1 = read_sensor1(ds_object)
        sensor2 = read_sensor2(ds_object)
        sensor3 = read_sensor3(ds_object)
        #os.system('rmmod w1-gpio')
        #os.system('rmmod w1-therm')

        #Transmit to google app engine
        try:
                transmit(tank_id, sensor1, sensor2, sensor3)
        except: 
                logging.debug('Could not transmit!')

        #Sleepy weepy!
        time.sleep(60)
