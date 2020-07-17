# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = cv2.imread('image1.jpg')

res1 = cv2.resize(img,
                 None,
                 fx = 2,
                 fy = 2,
                 interpolation = cv2.INTER_CUBIC)

height,width = img.shape[:2]
res2 = cv2.resize(img,
                 (2 * width,2 * height),
                 interpolation = cv2.INTER_CUBIC)

while True:
    cv2.imshow('res1',res1)
    cv2.imshow('res2',res2)
    cv2.imshow('img',img)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()