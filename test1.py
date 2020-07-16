# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt


image = cv2.imread('image3.jpg',)
image2 = cv2.imread('image4.jpg')

row,col,channels = image2.shape
roi = image[0:row, 0:col]

img2gray = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 175, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

image_bg = cv2.bitwise_and(roi, roi, mask = mask)
image2_fg = cv2.bitwise_and(image2, image2, mask = mask_inv)

dst = cv2.add(image_bg,image2_fg)
image[0:row, 0:col] = dst

cv2.imshow('Capoo', image)
cv2.waitKey(0)
cv2.destroyAllWindows()