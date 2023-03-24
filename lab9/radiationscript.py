import RPi.GPIO as GPIO
import datetime
import time
import sys

GPIO.setmode(GPIO.BCM)    
channel = 6
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

assert len(sys.argv) == 4, "use the correct number of arguments!"

file_name = sys.argv[3]
        
f = open(file_name, "w")

f.write("timestamp,")

f.write("counts per " + sys.argv[2] + " seconds")

f.write("\n")

startTime = time.time()

while time.time() - startTime < int(sys.argv[1]):
    c = 0
    loopTime = time.time()
    while time.time() - loopTime < int(sys.argv[2]):
        GPIO.wait_for_edge(channel, GPIO.FALLING)
        print("Radiation Detected At", str(datetime.datetime.now()))
        c = c+1
    print("Counts in the last " + sys.argv[2] + " seconds", c)
    f.write(str(time.time()) + ",")
    f.write(str(c))
    f.write("\n")

    
    
    
