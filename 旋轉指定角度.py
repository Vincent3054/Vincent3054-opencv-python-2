#-------------------------------------#
#旋轉指定角度#
import cv2
(h, w, d) = image.shape
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 180, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
viewImage(rotated, "旋轉180度後")
#image.shape顯示高,寬,channels. 
#M:從中心旋轉180度.
#-------------------------------------#