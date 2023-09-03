import RPi.GPIO as GPIO

def gray_decode(n):
    m = n >> 1
    while m:
        n ^= m
        m >>= 1
    return n

def GreyCodeRead():
    enc1 = GPIO.input(4)
    enc2 = GPIO.input(17)
    enc3 = GPIO.input(27)
    enc2 = enc2*10
    enc3 = enc3*100
    greyCode = enc1 + enc2 + enc3
    GameSelect = gray_decode(greyCode)
    return GameSelect