
#-------------------------------------#
#調整亮度#
import cv2
import numpy as np
img = cv2.imread('lena.jpg')
res = np.uint8(np.clip((1.5 * img + 10), 0, 255))
tmp = np.hstack((img, res))  # 兩張圖片橫向合併（便於對比顯示）
cv2.imshow('image', tmp)
cv2.waitKey(0)
#-------------------------------------#