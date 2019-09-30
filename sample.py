import numpy
import cv2




img = cv2.imread("lena.png")#lenna画像の読み込み
img2 = cv2.imread("lena.png",0)#グレースケールで読み込み。0はグレー1以上で3チャンネルカラー

cv2.imshow("color",img)#imgをcolorで表示
cv2.imshow("gray",img2)#img2をgrayで表示
cv2.waitKey(0)#キーボードからの入力待機で引数のミリ秒だけ入力を待ち受けてその後の処理に移る
cv2.destroyAllWindows()#現在表示中のhighGUIの画像表示を全て破棄する