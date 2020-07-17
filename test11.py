# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('HMimage.jpg')
rows, cols, ch = img.shape

markpoint = [[45, 1713], [1321, 537], [1657, 3573],[3009,2281]]
dstpoint = [[0, 0], [3024, 0], [0, 4032],[3023,4032]]

pts1 = np.float32(markpoint)
pts2 = np.float32(dstpoint)

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (3024,4032))

plt.subplot(221), plt.imshow(img), plt.title('Input')
plt.subplot(222), plt.imshow(dst), plt.title('Output')
plt.show()
