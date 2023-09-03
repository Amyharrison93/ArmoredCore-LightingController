import cv2 as cv
import numpy as np
import math


def CamStart():
    try:
        cam = cv.VideoCapture(0)
    except:
        cam = "Camera setup failed"
    ret, frame = cam.read()
    return cam

def ScaleAndCaptureFrame(cam):
    ret, frame = cam.read()
    frame = CropToFit(frame)
    return frame

def CropAspect16_9(frame):
    frameCentreVer, frameCentreHor, frameDepth = np.shape(frame)
    if(int(frameCentreHor/frameCentreVer) != int(16/9)):
        frameCentreHor = int(frameCentreHor/2)
        frameCentreVer = int(frameCentreVer/2)
        frame = frame[frameCentreHor-int(1280/2) : frameCentreHor+int(1280/2) , frameCentreVer-int(720/2) : frameCentreVer+int(720/2)]
    return frame

def CropToFit(frame):
    frame = cv.resize(frame, (1920, 1080))
    frameCentreVer, frameCentreHor, frameDepth = np.shape(frame)
    frameCentreHor = int(frameCentreHor/2)
    frameCentreVer = int(frameCentreVer/2)
    frame = frame[frameCentreVer-int(540/2) : frameCentreVer+int(540/2), frameCentreHor-int(960/2) : frameCentreHor+int(960/2)]
    frame = cv.resize(frame, (960, 540))
    return frame

def CropFrameHealth(frame):
    frame = frame[448:449,65:235]
    frame = cv.resize(frame, (960, 540))
    return frame

def CropFrameStun(frame):
    frame = frame[449:451,479:481]
    frame = cv.resize(frame, (960, 540))
    return frame

def CropFrameDirectionForward(frame):
    frame = frame[409:451,479:481]
    frame = cv.resize(frame, (960, 540))
    cv.imshow("", frame)
    cv.waitKey(1)
    return frame