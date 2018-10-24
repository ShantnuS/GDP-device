#Main script for reading and trasmitting temperatures 
import time

def read_temp():
    temp = 1
    #read temp somehow
    return temp

def transmit(temp):
    #transmit temp somehow 
    return True

def main():
    while True:
        temp = read_temp()
        transmit(temp)
        time.sleep(60)