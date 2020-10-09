import cv2 as cv
import sys
def main(video):
    low = {"H":32,"S":80,"V":62}
    high = {"H":114,"S":255,'V':132}
    window_cap_name = "Source"
    window_out_name = "Output"
    cv.namedWindow(window_cap_name)
    cv.namedWindow(window_out_name)
    key = cv.waitKey(10)
    while True:
        ret,frame = video.read()
        if frame is None:
            break
        if key == ord('p'):
            cv.waitKey(-1)
        frame_HSV = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        frame_threshold = cv.inRange(frame_HSV,(low["H"],low["S"],low["V"]),(high["H"],high['S'],high["V"]))
        cv.imshow(window_cap_name, frame)
        cv.imshow(window_out_name, frame_threshold)
        if key == ord('q') or key == 27:
            break
          
if __name__ == "__main__":
    ## Add video path to the command
    video = sys.argv[1]
    cap = cv.VideoCapture(video)
    main(cap)