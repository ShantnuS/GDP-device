#Main script for reading and trasmitting temperatures 
import time

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

def main():
    while True:
        temp = read_temp()
        transmit(temp)
        time.sleep(60)