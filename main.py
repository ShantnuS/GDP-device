#Main script for reading and trasmitting temperatures 
import time
import json
import urllib.request

def read_temp():
    temp1 = 1
    temp2 = 2
    temp3 = 3
    #read temp somehow
    return [temp1,temp2,temp3]

def transmit(temp):
    #transmit temp somehow
    temp1 = temp[0]
    print("Transmitted!!!!") 
    return True

def trasmit_test(tank_id, sensor1, sensor2, sensor3):
    body = {'tankId': tank_id, 'sensor1': sensor1, 'sensor2': sensor2, 'sensor3': sensor3, 'timeTaken': '4343'}
    myurl = "http://iglooboiler.appspot.com/readings"
    req = urllib.request.Request(myurl)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    response = urllib.request.urlopen(req, jsondataasbytes)
    return response

def get_test():
    item  = json.load(urllib.request.urlopen('http://iglooboiler.appspot.com/readings'))
    return item

def main(tank_id):
    print(trasmit_test(tank_id, 11,22,33))
    #print(get_test())


'''
    while True:
        temp = read_temp()
        transmit(temp)
        time.sleep(60)
'''