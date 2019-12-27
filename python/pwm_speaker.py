#!/usr/bin/python
import RPi.GPIO as GPIO
import time, datetime

GPIO.setmode(GPIO.BCM)

taste1 = 18
GPIO.setup(taste1, GPIO.IN, GPIO.PUD_DOWN)
taste2 = 4
GPIO.setup(taste2, GPIO.IN, GPIO.PUD_DOWN)
speaker = 17
GPIO.setup(speaker, GPIO.OUT)
pwm = GPIO.PWM(speaker, 440)
pwm.start(50)

try:
    print("Zum Start des Countdowns Taste 1 drücken!")
    print("Zum Beenden Taste 2 drücken!")
    
    while True:
        for x in range(100):
            time.sleep(.1)
            pwm.ChangeDutyCycle(x)
            
        for x in range(100):
            time.sleep(.1)
            pwm.ChangeDutyCycle(100-x)
        
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

