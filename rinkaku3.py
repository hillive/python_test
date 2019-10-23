#色中抽出リアルタイム動画保存 
import numpy as np
import cv2 as cv

#動画の読み込み
cap = cv.VideoCapture(0)


size=(640,480)#録画する動画のフレームサイズを(webカメラと同じにする)
fps = 20#1秒間に20枚のフレーム数
fourcc = cv.VideoWriter_fourcc(* 'XVID')

out = cv.VideoWriter('./movie/test3.avi',fourcc,fps,size)

if not cap.isOpened():
    print("Cannot open camera")
    exit()


while(1):
    _, frame = cap.read()#_,の意味ret,との違い
    
    #サイズ変更
    #frame = cv.resize(frame, dsize=(500,500))

    #HSVに変換
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    #白のHSV範囲(取得する色の範囲を指定するおそらく2値化)
    lower_white = np.array([0,0,100])#???np.arrayの使いかた
    upper_white = np.array([180,45,255])

    #白以外にマスク
    mask_white = cv.inRange(hsv,lower_white,upper_white)##??inRange(指定した色に基づいたマスク画像の生成)
    res_white = cv.bitwise_and(frame,frame,mask=mask_white)##??bitwise(フレーム画像とマスク画像の共通の領域を抽出する)
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
    img = cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)


    #再生
    cv.imshow('video',img)
    out.write(frame)#書き込み
    k = cv.waitKey(25) & 0xFF

    if k == ord('q'):
        break


#When everything done, release the capture
cap.release()
out.release()
cv.destroyAllWindows()



