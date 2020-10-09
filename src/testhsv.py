import cv2 as cv
import sys

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
        cv.imshow(src_window, frame)
        cv.imshow(dst_window, frame_threshold)
        if key == ord('q') or key == 27:
            break
    video.release()
    cv.destroyAllWindows()
          
if __name__ == "__main__":
    ## Add video path to the command
    ##video = sys.argv[1]
    cap = cv.VideoCapture(r'../footage/chipper.mp4')
    main(cap)