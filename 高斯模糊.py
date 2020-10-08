
#-------------------------------------#
#高斯模糊#
import cv2
blurred = cv2.GaussianBlur(image, (51, 51), 0)
viewImage(blurred, "Blurred doggo")
#image是要模糊化的圖片名稱
#(51, 51)必須為正奇數，數字越高照片越模糊
#0: sigmaX and sigmaY，預設值即可
#-------------------------------------#