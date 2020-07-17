# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = cv2.imread('image1.jpg',0)
rows, cols = img.shape

M = np.float32([[1, 0, 200], [0, 1, 100]])
dst = cv2.warpAffine(img, M, (cols, rows))

while True:
    cv2.imshow('dst',dst)
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
    