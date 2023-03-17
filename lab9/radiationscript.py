# coding=utf-8
 
import RPi.GPIO as GPIO
import datetime
import time
 
def my_callback(channel):
    if GPIO.input(channel) == GPIO.HIGH:
        print('\n▼  at ' + str(datetime.datetime.now()))
    else:
        print('\n ▲ at ' + str(datetime.datetime.now())) 
 
 
for i in range(0,30):
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(6, GPIO.IN)
        GPIO.add_event_detect(6, GPIO.BOTH, callback=my_callback)
     
        message = input('\nPress any key to exit.\n')
     
    finally:
        GPIO.cleanup()
        
    time.sleep(1)
 
print("Goodbye!")
