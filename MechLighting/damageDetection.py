import cv2 as cv
import numpy as np
import math

def DetectDamage(frame):
    boundaries = [
        ([17, 15, 100], [50, 56, 200]),
    ]
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype = "uint8")

        mask = cv.inRange(frame, lower, upper)
        return math.mean(mask)
        
def DetectHealth(frame):
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame = cv.threshold(frame,127,255,cv.THRESH_BINARY)
    health = math.mean(frame)
    return health