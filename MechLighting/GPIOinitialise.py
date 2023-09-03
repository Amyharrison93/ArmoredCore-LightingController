import RPi.GPIO as GPIO

def GPIOModeSet():
    GPIO.setmode(GPIO.BCM)
    #encoder setup
    GPIO.setup(4, GPIO.IN)
    GPIO.setup(17, GPIO.IN)
    GPIO.setup(27, GPIO.IN)
    #output setup
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)