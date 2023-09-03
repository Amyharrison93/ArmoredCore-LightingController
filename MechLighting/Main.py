import RPi.GPIO as GPIO
import GreyCode
import ImagePreProcess as imgGet
import GPIOinitialise as gpioInit

gpioInit.GPIOModeSet()

while 1:
    enc1 = GPIO.input(4)
    enc2 = GPIO.input(17)
    enc3 = GPIO.input(27)
    enc2 = enc2*10
    enc3 = enc3*100
    greyCode = enc1 + enc2 + enc3
    GameSelect = GreyCode.gray_decode(greyCode)
    print(GameSelect)

    if(GameSelect == 1):
        #do armored core stuff
        GPIO.output(18, 1)
        frame = imgGet.ScaleAndCaptureFrame()
        healthBar = imgGet.CropFrameHealth()
    elif(GameSelect == 2):
        #do mechwarrour stuff
        GPIO.output(23, 0)
    
    if(GPIO.input(21) == 1):
        break