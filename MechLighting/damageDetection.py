import cv2 as cv
import numpy as np
import RPi.GPIO as GPIO

def DetectDamage(frame):
    boundaries = [
        ([0, 0, 150], [0, 0, 200]),
    ]
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype = "uint8")

        mask = cv.inRange(frame, lower, upper)
        
        return np.mean(mask, axis=(0, 1))

def DetectLowHealth(frame, pin):
    boundaries = [
        ([0, 0, 200], [0, 0, 255]),
    ]
    GPIO.output(pin, 1)
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype = "uint8")

        mask = cv.inRange(frame, lower, upper)
        health = np.mean(mask, axis=(0, 1))
        if(health > 0):
            health = health/255
            health = health*100
        else:
            health = 0
        return health

def DamageDirection(frame):
    boundaries = [
        ([0, 0, 200], [0, 0, 255]),
    ]
    GPIO.output(pin, 1)
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype = "uint8")

        mask = cv.inRange(frame, lower, upper)
        
def DetectHealth(frame):
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    ret, frame = cv.threshold(frame,127,255,cv.THRESH_BINARY)
    health = np.mean(frame, axis=(0, 1))
    if(health > 0):
        health = health/255
        health = health*100
    return health