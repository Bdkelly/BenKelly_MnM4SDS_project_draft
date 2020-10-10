import cv2 as cv
import numpy as np


def main(video):
    low = {"H":32,"S":80,"V":62}
    high = {"H":114,"S":255,'V':132}
    src_window = "Source"
    dst_window = "Output"
    building(video,high,low,src_window,dst_window)

def building(video,high,low,src_window,dst_window):
    cv.namedWindow(src_window)
    cv.namedWindow(dst_window)
    while True:
        ret,frame = video.read()
        if frame is None:
            break
        key = cv.waitKey(10)
        if key == ord('p'):
            cv.waitKey(-1)
        frame_HSV = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        frame_threshold = cv.inRange(frame_HSV,(low["H"],low["S"],low["V"]),(high["H"],high['S'],high["V"]))
        canimg = hough(frame_HSV)
        ##cv.imshow(src_window, frame)
        cv.imshow(dst_window, frame_threshold)
        cv.imshow("NewFrame",canimg)
        if key == ord('q') or key == 27:
            break
    video.release()
    cv.destroyAllWindows()

def hough(frame):
    newimg = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    canimg = cv.Canny(newimg,50,200)
    lines = cv.HoughLines(canimg,1,np.pi/180,120,np.array([]))
    for line in lines:
        rho,theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0+1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 -1000*(-b))
        y2 = int(y0 - 1000 *(1))
        cv.line(frame, (x1,y1), (x2,y2), (0,0,255), 2)
    #cv.imshow("Lines",frame)
    #cv.imshow("Canny",canimg)
    #cv.waitKey(0)
    return canimg

if __name__ == "__main__":
    video = cv.VideoCapture(r"../footage/longgame.mp4")
    main(video)