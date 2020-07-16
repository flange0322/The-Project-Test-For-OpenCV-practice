# -*- coding: utf-8 -*-
import numpy as np
import cv2

img = np.zeros([512,512,3],np.uint8)

img_line = cv2.line(img,(0,0),(511,511),(255,0,0),5)
img_rectangle = cv2.rectangle(img, (384,0), (510,128), (0,255,0),3)
img_circle = cv2.circle(img, (447,63), 63, (0,0,255), -1)
img_ellipas = cv2.ellipse(img, (256,256), (100,50),0,0,180,255,-1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img_polylines = cv2.polylines(img,[pts], True,(0,255,255),4)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Chihuahua',(10,500), font, 2,(255,255,255),5)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

