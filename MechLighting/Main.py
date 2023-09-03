import RPi.GPIO as GPIO
import cv2 as cv
import GreyCode
import ImagePreProcess as imgGet
import GPIOinitialise as gpioInit
import damageDetection as dmgDetect
import Games

gpioInit.GPIOModeSet()
cam = imgGet.CamStart()

while 1:
    GameSelect = GreyCode.GreyCodeRead()
    print(GameSelect)

    GameSelect = 1

    if(GameSelect == 1):
        #do armored core stuff
        Games.ArmoredCore6(cam)

    elif(GameSelect == 2):
        #do mechwarrour stuff
        GPIO.output(23, 0)
    
    if(GPIO.input(21) == 1):
        break
    if cv.waitKey(1) == ord('q'):
        break
cv.destroyAllWindows()

def ArmoredCore6():
    GPIO.output(18, 1)
    frame = imgGet.ScaleAndCaptureFrame(cam)
    healthBar = imgGet.CropFrameHealth(frame)
    health = dmgDetect.DetectHealth(healthBar, )
    dmgTaken = dmgDetect.DetectDamage(healthBar)

    print("damage taken = ", dmgTaken)
    print("health remaining: ", health)
    return