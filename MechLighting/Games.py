import RPi.GPIO as GPIO
import ImagePreProcess as imgGet
import damageDetection as dmgDetect

def ArmoredCore6(cam):
    frame = imgGet.ScaleAndCaptureFrame(cam)
    healthBar = imgGet.CropFrameHealth(frame)
    health = dmgDetect.DetectHealth(healthBar, 23)
    dmgTaken = dmgDetect.DetectDamage(healthBar)

    if(dmgTaken > 0):
        GPIO.output(18, 1)
    else:
        GPIO.output(18, 0)
        
    print("damage taken = ", dmgTaken)
    print("health remaining: ", health)