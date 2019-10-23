#webカメラ撮影

import numpy as np
import cv2 as cv 

cap = cv.VideoCapture(0)

while True:#while Ture = While(cap.isOpened())
    ret,frame = cap.read()#Capture frame-by-frame/_,=ret,

    cv.imshow('frame',frame)#画面表示

    if cv.waitKey(1) == ord('q'):#キー入力待機
        break

cap.release()
cv.destroyAllWindows()