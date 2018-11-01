#!/bin/sh

#Ready up the gpio pins 
sudo modprobe w1-gpio
sudo modprobe w1-therm

# This is the code to initialise the python scripts on the Pi Zero device 
sudo python3 ~/GDP-device/boot.py & 
sudo python3 ~/GDP-device/updater.py & 
