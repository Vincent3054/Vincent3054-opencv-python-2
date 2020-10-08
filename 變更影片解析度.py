#-------------------------------------#
#變更影片解析度#
import cv2
cap = cv2.VideoCapture(1)
# 設定影像的尺寸大小
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)
while(True):
  ret, frame = cap.read()
  cv2.imshow('frame', frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
#-------------------------------------#

