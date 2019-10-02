import cv2 as cv

video_path = "./movie/sample.avi"
cap = cv.VideoCapture(video_path)

num = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv.imwrite("./img/picture{:0=3}".format(num)+".jpg",frame)
        print("save picture{:0=3}".format(num)+".jpg")
        num += 1
    else:
        break

cap.release()