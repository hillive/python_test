#色中画像
import numpy as np
import cv2 as cv

#画像の読み込み
src = cv.imread('./img2/ios_test.jpg')

#HSVに変換
hsv = cv.cvtColor(src,cv.COLOR_BGR2HSV)

#白のHSV範囲(取得する色の範囲を指定するおそらく2値化)
lower_white = np.array([0,0,100])#???np.arrayの使いかた
upper_white = np.array([180,45,255])

#白以外にマスク
mask_white = cv.inRange(hsv,lower_white,upper_white)##??inRange(指定した色に基づいたマスク画像の生成)
res_white = cv.bitwise_and(src,src,mask=mask_white)##??bitwise(フレーム画像とマスク画像の共通の領域を抽出する)
cv.imwrite('result1.jpg',res_white)

#グレースケール化
gray = cv.cvtColor(res_white,cv.COLOR_RGB2GRAY)

#2値化
ret,thresh = cv.threshold(gray,45,255,cv.THRESH_BINARY)

#輪郭抽出
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

#一番大きい輪郭のみを抽出
contours.sort(key=cv.contourArea,reverse=True)
cnt = contours[0]

#最小外接四角形を描画
x,y,w,h = cv.boundingRect(cnt)
img = cv.rectangle(src,(x,y),(x+w,y+h),(0,255,0),2)

cv.imwrite('reslt2.jpg',img)
