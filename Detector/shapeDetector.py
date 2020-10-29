# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 22:21:55 2020

@author: Ashok
"""

import cv2

class ShapeDetector:
    def __init__(self):
        pass
    
    def detect(self, c):
        shape = "unidentified"
        perimeter = cv2.arcLength(c, True)
        contour_approx = cv2.approxPolyDP(c, 0.04 * perimeter, True)
        
        if len(contour_approx) == 3:
            shape = "Triangle"
            
        #contour consists of a list of vertices; Based on the number of vertices, the shape is detected.
        #Both the sqaure and rectangle has 4 vertices. To predict whether sqaure or rectangle, we calculate 
        #the aspect ratio of the contour by dividing with to height. if aspect_ratio ~ 1.0 then square, else rect.
        elif len(contour_approx) == 4:
            (x, y, w, h) = cv2.boundingRect(contour_approx)
            asp_rat = w / float(h)
            shape = "Sqaure" if asp_rat >= 0.95 and asp_rat <= 1.05 else "Rectangle"
        
        elif len(contour_approx) == 5:
            shape = "Pentagon"
        
        else:
            shape = "Circle"
        
        return shape
    
    
            