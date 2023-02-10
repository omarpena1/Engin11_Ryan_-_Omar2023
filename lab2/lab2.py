import adafruit_bme680
import time
import board
import pandas as pd

i2c = board.I2C()

bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)
bme680.sea_level_pressure = 1013.25

timebegin = []
temperature = []
gas = []
pressure = []
humidity = []
altitude = []

for i in range(0, 30):
	#print("\nTemperature: %0.1f C" % bme680.temperature)
	#print("Gas: %d ohm" % bme680.gas)
	#print("Humidity: %0.1f %%" % bme680.relative_humidity)
	#print("Pressure: %0.3f hPa" % bme680.pressure)
	#print("Altitude = %0.2f meters" % bme680.altitude)
	
	#print(i * 2, bme680.temperature, bme680.gas, bme680.relative_humidity, bme680.pressure, bme680.altitude)
	timebegin.append(i * 2)
	temperature.append(bme680.temperature)
	gas.append(bme680.gas)
	pressure.append(bme680.pressure)
	humidity.append(bme680.relative_humidity)
	altitude.append(bme680.altitude)
	print("done")
	time.sleep(2)

columndict = {"Time" : timebegin, "Temperature" : temperature, "Gas" : gas, "Pressure" : pressure, "Humidity" : humidity, "Altitude" : altitude}

df = pd.DataFrame(columndict)

df.to_csv("lab2sensordatafeb32023.csv")
