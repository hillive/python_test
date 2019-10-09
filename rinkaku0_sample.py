import numpy as np
import cv2 as cv

img = cv.imread('test.jpg')

new = cv.drawContours(img,contours,-1,(255,0,0),3)

cv.imwrite('output1.jpg',new)#save


##これだとline6が怒られる。おそらくfindContoursをしてないからだと思う