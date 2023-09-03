import RPi.GPIO as GPIO
import ImagePreProcess as imgGet
import damageDetection as dmgDetect
healthLED = 23
damageLED = 18

def ArmoredCore6(cam):
    frame = imgGet.ScaleAndCaptureFrame(cam)
    healthBar = imgGet.CropFrameHealth(frame)
    stunBar = imgGet.CropFrameStun(frame)

    health = dmgDetect.DetectHealth(healthBar, healthLED)
    dmgTaken = dmgDetect.DetectDamage(healthBar)
    if(dmgTaken > 0):
        GPIO.output(damageLED, 1)
    else:
        GPIO.output(damageLED, 0)
        
    print("damage taken = ", dmgTaken)
    print("health remaining: ", health)