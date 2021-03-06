#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
 
# Use GPIO numbering
GPIO.setmode(GPIO.BCM)
 
# Set GPIO for camera LED
# Use 5 for Model A/B and 32 for Model B+
CAMLED = 32
 
# Set GPIO to output
GPIO.setup(CAMLED, GPIO.OUT, initial=False) 
 
GPIO.output(CAMLED,False) # Off

