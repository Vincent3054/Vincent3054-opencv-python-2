
#-------------------------------------#
#灰階效果#
import cv2
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, threshold_image = cv2.threshold(im, 127, 255, 0)
viewImage(gray_image, "Gray-scale doggo")
viewImage(threshold_image, "Black & White doggo")
#ret, threshold = cv2.threshold(im, 150, 200, 10)
#調整參數會有不同效果
#-------------------------------------#