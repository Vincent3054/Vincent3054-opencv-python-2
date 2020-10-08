

#-------------------------------------#
#匹配圖片#
import cv2
#用模板圖片去尋找圖片中的物件
#讀入原圖和模板
img_rgb = cv2.imread('mario.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('mario_coin.jpg', 0)
h, w = template.shape[:2]
#標準相關模板匹配
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)  # 匹配程度大於%80的坐標y,x
for pt in zip(*loc[::-1]):  # *號表示可選參數
right_bottom = (pt[0] + w, pt[1] + h)
cv2.rectangle(img_rgb, pt, right_bottom, (0, 0, 255), 2)
#-------------------------------------#