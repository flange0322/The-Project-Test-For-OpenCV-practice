# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt


image = cv2.imread('image1.jpg')
image2 = cv2.imread('image2.jpg')

dst = cv2.addWeighted(image, 0.7, image2, 0.3, 0)

cv2.imshow('Capoo', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()