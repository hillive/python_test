#webカメラ制御&撮影&保存

import numpy as np
import cv2 as cv 

cap = cv.VideoCapture(0)

size=(640,480)#録画する動画のフレームサイズを(webカメラと同じにする)
fps = 20#1秒間に20枚のフレーム数
fourcc = cv.VideoWriter_fourcc(* 'XVID')

out = cv.VideoWriter('./movie/sample.avi',fourcc,fps,size)


if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:#while Ture = While(cap.isOpened())
    ret,frame = cap.read()#Capture frame-by-frame

    #if frame is read correctly ret is True
    if not ret:
        print("Cant't recive frame(stream end?).Exiting...")
        break

    cv.imshow('frame',frame)#画面表示

    out.write(frame)#書き込み

    if cv.waitKey(1) == ord('q'):#キー入力待機
        break

#When everything done, release the capture
cap.release()
out.release()
cv.destroyAllWindows()