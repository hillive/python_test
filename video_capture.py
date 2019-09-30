import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)#カメラで動画を撮影







cv.imshow('frame' frame)
if cv.waitKey(1) ==ord('q'):
    break

cap.release()
out.release()
cv.destroyAllWindows()

