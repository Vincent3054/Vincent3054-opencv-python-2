import numpy as np
import cv2

#-------------------------------------#
#讀取圖檔#
img = cv2.imread('a.jpeg')
#以 cv2.imread 讀進來的資料，會存成NumPy陣列
# 以灰階的方式讀取圖檔
img_gray = cv2.imread('a.jpg', cv2.IMREAD_GRAYSCALE) 
#cv2.IMREAD_COLOR     為預設值
#cv2.IMREAD_GRAYSCALE 以灰階的格式來讀取圖片。 
#cv2.IMREAD_UNCHANGED 讀取圖片中所有的 channels，包含透明度的 channel。
#-------------------------------------#

#-------------------------------------#
#查看圖片屬性#
#1920×1080的彩色圖片
img.shape(1080, 1920, 3)      
#(圖片高度,圖片寬度,RGB維度) RGB微度彩色為3，灰階為1
#-------------------------------------#

#-------------------------------------#
#建立特徵分類器#
faceCascade = cv2.CascadeClassifier(cascPath)
#cascPath為一個XML檔
#-------------------------------------#

#-------------------------------------#
#偵測圖片#
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)
#detectMultiScale為偵測特徵的功能
#gray是灰階圖片
#scaleFactor圖像縮放比例，類似相機X倍鏡頭
#minNeighbors針對特徵點附近進行檢測
#minSize特徵檢測點的最小尺寸 
#scaleFactor,minNeighbors,minSize數值大小將影響辨識結果，須依狀況進行實驗
#-------------------------------------#

#-------------------------------------#
#繪製方框#
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#(0, 255, 0)欄位可以變更方框顏色(Blue,Green,Red)
#轉換成RGB格式
#rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#-------------------------------------#

#-------------------------------------#
#在圖片內畫線#
import cv2
output = image.copy()
cv2.line(output, (60, 20), (400, 200), (0, 0, 255), 5)
viewImage(output, "2 Doggos separated by a line")
#output為要畫線的圖片名稱
#(60, 20)=(x1, y1)
#(400, 200)=(x2, y2)
#(0, 0, 255)為線條顏色(GBR或RGB，取決於是否使用cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
#5 為線條粗細度

cv2.line()畫直線
cv2.circle()畫圓
cv2.rectangle()畫矩形
cv2.ellipse()畫橢圓
cv2.polylines()畫多邊形
#-------------------------------------#

#-------------------------------------#
# 顯示圖片#
cv2.imshow('My Image', img)
cv2.waitKey(0)                #持續等待至使用者按下按鍵為止（單位為毫秒）              
cv2.destroyAllWindows()       #關閉所有視窗
cv2.destroyWindow('My Image') #關閉My Image視窗
#-------------------------------------#





