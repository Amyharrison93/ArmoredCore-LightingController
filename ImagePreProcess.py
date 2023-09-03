import cv2 as cv
import numpy as np
import math

def ScaleAndCaptureFrame():
    try:
        cam = cv.VideoCapture(cv.intCamLoc, cv.CAP_DSHOW)
    except:
        cam = "Camera setup failed"

    ret, frame = cam.read()
    frame = cv.resize(frame, (1280, 720))
    return frame

def CropFrameHealth(frame):
    frame = frame[400:700,500:550]
    return frame

