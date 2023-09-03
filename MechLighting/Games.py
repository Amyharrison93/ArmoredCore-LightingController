import RPi.GPIO as GPIO
import ImagePreProcess as imgGet
import damageDetection as dmgDetect
healthLED = 23
damageLED = 18
stunLED = 24
stunnedLED = 25

def ArmoredCore6(cam):
    frame = imgGet.ScaleAndCaptureFrame(cam)
    healthBar = imgGet.CropFrameHealth(frame)
    stunBar = imgGet.CropFrameStun(frame)

    fwdWarning = imgGet.CropFrameDirectionForward(frame)

    health = dmgDetect.DetectHealth(healthBar, healthLED)
    dmgTaken = dmgDetect.DetectDamage(healthBar, damageLED)
    stunTaken = dmgDetect.DetctStun(stunBar, stunLED, stunnedLED)

    fwdWarn = dmgDetect.DamageDirection(fwdWarning)
        
    print("damage taken = ", dmgTaken)
    print("stun taken = ", stunTaken)
    print("health remaining: ", health)