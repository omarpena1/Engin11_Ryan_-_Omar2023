import time
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_pm25.i2c import PM25_I2C


reset_pin = None

import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.95)

from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, reset_pin)

import time

f = open("airpollutiondata.csv", "w")

metadata = ["time", "Concentration Units (Standard) PM 1.0","Concentration Units (Standard) PM 2.5","Concentration Units (Standard) PM 10.0"]

for entry in metadata:
    f.write(entry + ",")

f.write("\n")

print("Found PM2.5 sensor, reading data...")

for _ in range(30):
    time.sleep(1)
    
    try:
        aqdata = pm25.read()
        # print(aqdata)
    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue
    
    numbersdata = []
    itime = time.time()
    numbersdata.append(itime)
    
    print(aqdata["pm10 standard"])
    print(aqdata["pm25 standard"])
    print(aqdata["pm100 standard"])
    
    numbersdata.append(aqdata["pm10 standard"])
    numbersdata.append(aqdata["pm25 standard"])
    numbersdata.append(aqdata["pm100 standard"])

    
    for idata in numbersdata:
        f.write(str(idata)+",")

    f.write("\n")

f.close()
