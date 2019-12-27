#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
seg = 13
zif=[16, 12, 7, 6]
count = len(zif)

GPIO.setup(seg, GPIO.OUT, initial=1)

for z in range(count):
    GPIO.setup(zif[z], GPIO.OUT, initial=1)
    
print("STRG+C beendet das Programm")
try:
    while True:
        for i in range(count):
            GPIO.output(zif[i],0)
            time.sleep(0.2)
            GPIO.output(zif[i], 1)
            
except KeyboardInterrupt:
    GPIO.cleanup()
