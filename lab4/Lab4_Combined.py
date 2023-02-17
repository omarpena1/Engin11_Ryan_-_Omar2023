#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import adafruit_bme680
import time
import board
import pandas as pd
import busio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_pm25.i2c import PM25_I2C
import sys


i2c = board.I2C()

bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)
bme680.sea_level_pressure = 1013.25

# timebegin = []
# temperature = []
# gas = []
# pressure = []
# humidity = []
# altitude = []

# for i in range(0, 30):
# 	timebegin.append(time.time())
# 	temperature.append(bme680.temperature)
# 	gas.append(bme680.gas)
# 	pressure.append(bme680.pressure)
# 	humidity.append(bme680.relative_humidity)
# 	altitude.append(bme680.altitude)
# 	print("done")
# 	time.sleep(2)

#Lab 1 above Lab 2 below

reset_pin = None

import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.95)

from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, reset_pin)

# Create library object, use 'slow' 100KHz frequency!
#i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
# Connect to a PM2.5 sensor over I2C
#pm25 = PM25_I2C(i2c, reset_pin)

# import time

file_name = "PRELAB4data_tbl"

if( len(sys.argv)>2):
     file_name = sys.argv[1]
        
f = open(file_name, "w")

metadata = ["time", "Concentration Units (Standard) PM 1.0","Concentration Units (Standard) PM 2.5","Concentration Units (Standard) PM 10.0","temperature", "gas", "pressure", "humidity", "altitude"]

for entry in metadata:
    f.write(entry + ",")

f.write("\n")

# print("Found PM2.5 sensor, reading data...")

for _ in range(int(sys.argv[2]):
    
    
    try:
        aqdata = pm25.read()
        # print(aqdata)
    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue
    
    numbersdata = []
    itime = int(time.time())
    numbersdata.append(itime)
    
    print(aqdata["pm10 standard"])
    print(aqdata["pm25 standard"])
    print(aqdata["pm100 standard"])
    
    numbersdata.append(aqdata["pm10 standard"])
    numbersdata.append(aqdata["pm25 standard"])
    numbersdata.append(aqdata["pm100 standard"])
    numbersdata.append(bme680.temperature)
    numbersdata.append(bme680.gas)
    numbersdata.append(bme680.pressure)
    numbersdata.append(bme680.relative_humidity)
    numbersdata.append(bme680.altitude)

    
    for idata in numbersdata:
        f.write(str(idata)+",")

    f.write("\n")
               
    time.sleep(1)

f.close()