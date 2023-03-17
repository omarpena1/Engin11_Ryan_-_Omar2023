import RPi.GPIO as GPIO
import datetime
import time

GPIO.setmode(GPIO.BCM)    
channel = 6
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    c = 0
    startTime = time.time()
    while (time.time() - startTime < 60):
        c = c+1
        GPIO.wait_for_edge(channel, GPIO.FALLING)
        print("Radiation Detected At", str(datetime.datetime.now()))
    print("Counts Last Minute", c)
    
    
    
    
