#動画のプロパティを取得
import cv2 as cv

video_path = "./movie/output.avi"
cap = cv.VideoCapture(video_path)

width = cap.get(cv.CAP_PROP_FRAME_WIDTH)#幅
height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)#高さ
count = cap.get(cv.CAP_PROP_FRAME_COUNT)# 総フレーム数
fps = cap.get(cv.CAP_PROP_FPS)#fps

print("width:{}, height:{}, count:{}, fps:{}".format(width,height,count,fps))