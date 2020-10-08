
#-------------------------------------#
#加入英文字#
import numpy as np
import cv2

img = np.zeros((400, 400, 3), np.uint8)
img.fill(90)

# 文字
text = 'Hello, OpenCV!'

# 使用字體
# cv2.putText(影像, 要顯示的文字, 座標, 字型, 字體大小, 顏色, 線條寬度, 線條種類)
cv2.putText(img, text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX,
  1, (0, 255, 255), 1, cv2.LINE_AA)

cv2.imshow('My Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#-------------------------------------#

