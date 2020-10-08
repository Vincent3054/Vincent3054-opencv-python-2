#-------------------------------------#
#寫入圖片檔案#
# 寫入圖檔
cv2.imwrite('result.jpg', img)
# 寫入不同圖檔格式
cv2.imwrite('result.png', img)
cv2.imwrite('result.tiff', img)
# 設定 JPEG 圖片品質為 90（可用值為 0 ~ 100）
cv2.imwrite('output.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])
# 設定 PNG 壓縮層級為 5（可用值為 0 ~ 9）
cv2.imwrite('output.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 5])
#-------------------------------------#
