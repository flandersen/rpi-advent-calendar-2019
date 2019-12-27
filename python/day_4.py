#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

seg=[21, 13, 26]
count = len(seg)

for s in range(count):
    GPIO.setup(seg[s], GPIO.OUT, initial=0)

print("STRG+C beendet das Programm")
try:
    while True:
        for i in range(count):
            GPIO.output(seg[i],1)
            time.sleep(0.2)
            GPIO.output(seg[i], 0)
            
except KeyboardInterrupt:
    GPIO.cleanup()