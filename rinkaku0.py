import numpy as np
import cv2 as cv
#import matplotlib.pyplot as plt#matplolibライブラリーをインポート(matplotlibを使う宣言)
#from matplotlib.patches import polygon

#ファイル読み込み
src = cv.imread('./img2/bottole.jpg')

#グレースケール化
img_gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
cv.imwrite('debug1.png',img_gray)

#2値化
ret,dst = cv.threshold(img_gray,127,255,0)
cv.imwrite('debug2.png',dst)

#白黒反転
dst = cv.bitwise_not(dst)
cv.imwrite('debug3.png',dst)

#再度フィルタリング
#ret,dst = cv.threshold(dst,127,255,0)
#cv.imwrite('debug4.png',dst)

#輪郭抽出
contours,hierachy = cv.findContours(dst,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

#輪郭描画
dst = cv.drawContours(src,contours,-1,(0,255,0),2)
cv.imwrite('debug5.png',dst)



#外接短径を取得
#x,y,w,h = cv.boundingRect(contour)



#save
cv.imwrite('output3.jpg',dst)