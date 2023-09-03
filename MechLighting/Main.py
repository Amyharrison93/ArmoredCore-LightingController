import RPi.GPIO as GPIO
import GreyCode

GPIO.setmode(GPIO.BCM)
#encoder setup
GPIO.setup(4, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)
#LED setup
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

while 1:
    enc1 = GPIO.input(4)
    enc2 = GPIO.input(17)
    enc3 = GPIO.input(27)
    enc2 = enc2*10
    enc3 = enc3*100
    greyCode = enc1 + enc2 + enc3
    GameSelect = GreyCode.gray_decode(greyCode)

    if(GameSelect == 1):
        #do armored core stuff
        GPIO.output(18)
    elif(GameSelect == 2):
        #do mechwarrour stuff
        GPIO.output(23)