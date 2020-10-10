import cv2 as cv
import numpy as np

def main(video):
    while True:
        ret,frame = video.read()
        if frame is None:
            break
        canimg = hough(frame)
        cv.imshow("Lines",canimg)
        key = cv.waitKey(10)
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

if __name__  == "__main__":
    video = cv.VideoCapture(r"../footage/chipper.mp4")
    main(video)