# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 22:38:27 2020

@author: Ashok
"""

from Detector.shapeDetector import ShapeDetector
import imutils
import cv2

img = cv2.imread("input.png")
resized = imutils.resize(img, width=300)
ratio = img.shape[0] / float(resized.shape[0])

gray = cv2.cvtColor(resized, cv2.COLOR_RGB2GRAY)
blurred = cv2.GaussianBlur(gray, (5,5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
shape_det = ShapeDetector()

for c in contours:
    M = cv2.moments(c)
    #computes the center(x,y) of the contour
    cX = int((M["m10"] / M["m00"]) * ratio)
    cY = int((M["m01"] / M["m00"]) * ratio)
    
    shape = shape_det.detect(c)
    
    c = c.astype("float")
    c = c * ratio
    c = c.astype("int")
    cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
    cv2.putText(img, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),2)
    
    cv2.imshow("Output", img)
    cv2.waitKey(0)
    
    