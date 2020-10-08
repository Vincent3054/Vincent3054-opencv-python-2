#-------------------------------------#
#使用 Matplotlib 顯示圖片#
#彩色圖片
import numpy as np
import cv2
from matplotlib import pyplot as plt
# 使用 OpenCV 讀取圖檔
img_bgr = cv2.imread('image.jpg')
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
# 使用 Matplotlib 顯示圖片
plt.imshow(img_rgb)
plt.show()
#灰階圖片
# 使用 OpenCV 讀取灰階圖檔
img_gray = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
# 使用 Matplotlib 顯示圖片
plt.imshow(img_gray, cmap = 'gray')
plt.show()
#-------------------------------------#
