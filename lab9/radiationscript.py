import RPi.GPIO as GPIO
import datetime

channel = GPIO.wait_for_edge(channel, GPIO_FALLING)
print('Edge detected on channel', channel)