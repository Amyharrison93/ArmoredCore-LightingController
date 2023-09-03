import RPi.GPIO as GPIO
import cv2 as cv
import GreyCode
import ImagePreProcess as imgGet
import GPIOinitialise as gpioInit
import damageDetection as dmgDetect

gpioInit.GPIOModeSet()
cam = imgGet.CamStart()

while 1:
    enc1 = GPIO.input(4)
    enc2 = GPIO.input(17)
    enc3 = GPIO.input(27)
    enc2 = enc2*10
    enc3 = enc3*100
    greyCode = enc1 + enc2 + enc3
    GameSelect = GreyCode.gray_decode(greyCode)
    print(GameSelect)

    GameSelect = 1

    if(GameSelect == 1):
        #do armored core stuff
        GPIO.output(18, 1)
        frame = imgGet.ScaleAndCaptureFrame(cam)
        healthBar = imgGet.CropFrameHealth(frame)
        health = dmgDetect.DetectHealth(healthBar)
        dmgTaken = dmgDetect.DetectDamage(healthBar)
        print("damage taken = ", dmgTaken)
        if(health < 1):
            health = dmgDetect.DetectLowHealth(healthBar)
            print("warning low health ALARM")
        print("health remaining: ", health)
    elif(GameSelect == 2):
        #do mechwarrour stuff
        GPIO.output(23, 0)
    
    if(GPIO.input(21) == 1):
        break
    if cv.waitKey(1) == ord('q'):
        break
cv.destroyAllWindows()