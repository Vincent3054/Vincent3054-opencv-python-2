#-------------------------------------#
#邊緣檢測#
import cv2
import numpy as np
img = cv2.imread('handwriting.jpg', 0)
edges = cv2.Canny(img, 30, 70)  # canny邊緣檢測
cv2.imshow('canny', np.hstack((img, edges)))
cv2.waitKey(0)
#cv2.Canny()進行邊緣檢測，參數2、3表示最低、高閾值
#-------------------------------------#