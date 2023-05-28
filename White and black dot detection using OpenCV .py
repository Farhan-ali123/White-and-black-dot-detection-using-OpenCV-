import cv2 as cv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

path = "C:\\Users\\user\\Desktop\\newp\\venv\\resources\\white-dot.png"

# reading the image in grayscale mode
gray = cv.imread(path, 0)

# threshold
th, threshed = cv.threshold(gray, 100, 255,
                             cv.THRESH_BINARY | cv.THRESH_OTSU)

# findcontours
cnts = cv.findContours(threshed, cv.RETR_LIST,
                        cv.CHAIN_APPROX_SIMPLE)[-2]

# filter by area
s1 = 3
s2 = 20
xcnts = []

for cnt in cnts:
    if s1 < cv.contourArea(cnt) < s2:
        xcnts.append(cnt)

# printing output
print("\nDots number: {}".format(len(xcnts)))