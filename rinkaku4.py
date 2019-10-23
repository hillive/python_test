#色中抽出リアルタイム動画保存しない
import numpy as np
import cv2 as cv

#動画の読み込み
cap = cv.VideoCapture(0)


while(1):
    _, frame = cap.read()#_,の意味ret,との違い
    blurred_frame = cv.GaussianBlur(frame,(5,5),0)#おそさらく背景をぼかすbluerして背景のノイズを除いている。

    #HSVに変換
    hsv = cv.cvtColor(blurred_frame,cv.COLOR_BGR2HSV)

    #青のHSV範囲(取得する色の範囲を指定するおそらく2値化)
    lower_blue = np.array([38,86,0])#???np.arrayの使いかた
    upper_blue = np.array([121,255,255])

    #白以外にマスク
    mask_blue = cv.inRange(hsv,lower_blue,upper_blue)##??inRange(指定した色に基づいたマスク画像の生成)
    
    #dst = cv.bitwise_not(mask_white)#白黒反転
    contours, hierarchy = cv.findContours(mask_blue, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    
    for contour in contours:
        area = cv.contourArea(contour)#領域が占める面積を計算
        #print(area)

        if area > 10000:
            contours.sort(key=cv.contourArea,reverse=True)
            cnt = contours[0]
            x,y,w,h = cv.boundingRect(cnt)
            frame = cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            #cv.drawContours(frame,contours,-1,(0,255,0),3)
    
    cv.imshow("Frame",frame)
    cv.imshow("Mask",mask_blue)#本来はwhite_maskをshowするが白黒反転したやつをshowする。

    k = cv.waitKey(25) & 0xFF
    if k == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
    #res_white = cv.bitwise_and(frame,frame,mask=mask_white)##??bitwise(フレーム画像とマスク画像の共通の領域を抽出する)
    #cv.imwrite('result1.jpg',res_white)

    #グレースケール化
    #gray = cv.cvtColor(res_white,cv.COLOR_RGB2GRAY)

    #2値化
    #ret,thresh = cv.threshold(gray,45,255,cv.THRESH_BINARY)

    #輪郭抽出
    #contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


    #一番大きい輪郭のみを抽出
    #contours.sort(key=cv.contourArea,reverse=True)
    #cnt = contours[0]


    #最小外接四角形を描画
    #x,y,w,h = cv.boundingRect(cnt)
    #img = cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)


    #再生
    #cv.imshow('video',img)
    
    #k = cv.waitKey(25) & 0xFF

    #if k == ord('q'):
        #break


#cap.release()
#cv.destroyAllWindows()



