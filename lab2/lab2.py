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
	timebegin.append(time.time())
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
