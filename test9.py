# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = cv2.imread('image1.jpg')

rows, cols, colors = img.shape

M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 0.6)

dst = cv2.warpAffine(img, M, (cols, rows))

while True:
    cv2.imshow('dst',dst)
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
    