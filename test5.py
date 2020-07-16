# -*- coding: utf-8 -*-
import cv2
import numpy as np
img1 = cv2.imread('image3.jpg')
img2 = cv2.imread('image4.jpg')

'''
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2BGRA)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2BGRA)

capture = img2[100:400,100:400]
img1[100:400,500:800] = capture
'''

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)

lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

mask = cv2.inRange(img1,lower_blue,upper_blue)

res = cv2.bitwise_and(img1, img1,mask = mask)
cv2.imshow('img',img1)
cv2.imshow('mask',mask)
cv2.imshow('res',res)

cv2.waitKey(0)
cv2.destroyAllWindows()