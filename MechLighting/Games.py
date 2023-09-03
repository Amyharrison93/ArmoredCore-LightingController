import RPi.GPIO as GPIO
import ImagePreProcess as imgGet
import damageDetection as dmgDetect
healthIO = 23
damageIO = 18
stunIO = 24

def ArmoredCore6(cam):
    frame = imgGet.ScaleAndCaptureFrame(cam)
    healthBar = imgGet.CropFrameHealth(frame)
    stunBar = imgGet.CropFrameStun(frame)

    fwdWarning = imgGet.CropFrameDirectionForward(frame)

    health = dmgDetect.DetectHealth(healthBar, healthIO)
    dmgTaken = dmgDetect.DetectDamage(healthBar, damageIO)
    stunTaken = dmgDetect.DetctStun(stunBar, stunIO)

    fwdWarn = dmgDetect.DamageDirection(fwdWarning)
        
    print("damage taken = ", dmgTaken)
    print("stun taken = ", stunTaken)
    print("health remaining: ", health)