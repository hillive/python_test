#local画像のプロパティ取得&表示
import numpy as np
import cv2 as cv

img = cv.imread("lena.jpg")

height,width,ch = img.shape
#画素数 = 幅*高さ 
size = width*height

#情報表示
cv.imshow("color",img)
print("幅",width)
print("高さ",height)
print("チャンネル数",ch)
print("画素数",size)
print("データ型",img.dtype)

#1chずつ表示
print("Bの画素値:\n",img[:,:,0])
print("Gの画素値:\n",img[:,:,1])
print("Rの画素値:\n",img[:,:,2])

cv.waitKey(0)