import adafruit_bme680
import time
import board
import sys

i2c = board.I2C()

bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)
bme680.sea_level_pressure = 1013.25

import busio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_pm25.i2c import PM25_I2C

reset_pin = None

import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.95)

from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, reset_pin)

file_name = "mergedata.csv"
if (len(sys.argv) > 2):
        file_name = sys.argv[2] + file_name

f = open(file_name, "w")

metadata = ["time", "temperature", "gas", "pressure", "humidity", "altitude", "Concentration Units (Standard) PM 1.0","Concentration Units (Standard) PM 2.5","Concentration Units (Standard) PM 10.0"]

for entry in metadata:
    f.write(entry + ",")
    
f.write("\n")

start_time = time.time()

while time.time() < (start_time + sys.argv[1]):
        try:
                aqdata = pm25.read()
        except RuntimeError:
                print("Unable to read from sensor, retrying...")
                continue
        
        numbersdata = []
        numbersdata.append(time.time())
        numbersdata.append(bme680.temperature)
        numbersdata.append(bme680.gas)
	numbersdata.append(bme680.pressure)
	numbersdata.append(bme680.relative_humidity)
	numbersdata.append(bme680.altitude)
        numbersdata.append(aqdata["pm10 standard"])
        numbersdata.append(aqdata["pm25 standard"])
        numbersdata.append(aqdata["pm100 standard"])
        
        for idata in numbersdata:
                f.write(str(idata)+",")
        
        f.write("\n")
        
        time.sleep(2)

f.close()
        