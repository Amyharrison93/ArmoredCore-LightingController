import cv2 as cv
import numpy as np
import RPi.GPIO as GPIO

def DetectDamage(frame, pin):
    boundaries = [
        ([0, 0, 150], [0, 0, 200]),
    ]
    for (lower, upper) in boundaries:
        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype = "uint8")

        mask = cv.inRange(frame, lower, upper)
        dmgTaken = np.mean(mask, axis=(0, 1))

        if(dmgTaken > 0):
            GPIO.output(pin, 1)
        else:
            GPIO.output(pin, 0)
    return dmgTaken

def DetectLowHealth(frame, pin):
    boundaries = [
        ([0, 0, 200], [0, 0, 255]),
    ]
    
    for (lower, upper) in boundaries:
        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype = "uint8")

        mask = cv.inRange(frame, lower, upper)
        health = np.mean(mask, axis=(0, 1))
        if(health > 0):
            health = health/255
            health = health*100
            GPIO.output(pin, 1)
        else:
            health = 0
            GPIO.output(pin, 0)
    return health

def DamageDirection(frame):
    boundaries = [
        ([0, 0, 200], [0, 0, 255]),
    ]
    for (lower, upper) in boundaries:
        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype = "uint8")
        mask = cv.inRange(frame, lower, upper)
        mask = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
        damage = np.mean(mask, axis=(0, 1))

    return damage
        
def DetectHealth(frame, pin):
    grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    ret, grey = cv.threshold(grey,127,255,cv.THRESH_BINARY)
    health = np.mean(grey, axis=(0, 1))

    if(health <= 0):
        DetectLowHealth(frame, pin)
    else:
        GPIO.output(pin, 0)
    return health

def DetctStun(frame, pin, pin2):
    boundaries = [
        ([0, 0, 190], [15, 15, 255]),
    ]
    multiplier = 1
    for (lower, upper) in boundaries:
        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype = "uint8")
        mask = cv.inRange(frame, lower, upper)
        stun = np.mean(mask, axis=(0, 1)) * multiplier
        multiplier+= 1

    if(stun > 0):
        GPIO.output(pin, 1)
        GPIO.output(pin2, 0)
    elif(stun > 255):
        GPIO.output(pin, 0)
        GPIO.output(pin2, 1)
    else:
        GPIO.output(pin, 0)
        GPIO.output(pin2, 0)

    return stun