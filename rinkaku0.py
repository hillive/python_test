import numpy as np
import cv2 

img = cv2.imread('./test.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours,hierachy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

new = cv2.drawContours(imgray,contours,-1,(0,255,0),3)

cv2.imwrite('output.jpg',new)

cv2.waitKey(0)
cv2.destroyAllWindows()

##輪郭を描画した画像の保存ができない？？？