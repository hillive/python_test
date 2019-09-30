import numpy as np
import cv2 as cv 

cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(* 'XVID')
out = cv.VideoWriter('output.avi',fourcc,20.0,(640,480))


if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    #Capture frame-by-frame
    ret,frame = cap.read()

    #if frame is read correctly ret is True
    if not ret:
        print("Cant't recive frame(stream end?).Exiting...")
        break


    image = cv.cvtColor(frame,cv.COLOR_BGR2RGBA)

    #Display the resulting frame
    cv.imshow('frame',image)
    if cv.waitKey(1) == ord('q'):
        break

#When everything done, release the capture
cap.release()
out.release()
cv.destroyAllWindows()