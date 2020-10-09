import cv2 as cv
import sys

def main(video):
    low = {"H":32,"S":80,"V":62}
    high = {"H":114,"S":255,'V':132}
    src_window = "Source"
    dst_window = "Output"
    container = track(video)
    building(video,high,low,src_window,dst_window,container)

def track(video,num=3):
    track_xl = cv.MultiTracker_create()
    tri_dic = {'csrt':cv.TrackerCSRT_create,'kcf':cv.TrackerKCF_create,
                'boosting' : cv.TrackerBoosting_create,'mil': cv.TrackerMIL_create}
    ret, frame = video.read()
    for i in range(num):
        cv.imshow("Frame",frame)
        rec = cv.selectROI("Frame",frame)
        track = tri_dic["csrt"]()
        track_xl.add(track,frame,rec)
    return track_xl

def building(video,high,low,src_window,dst_window,trackers):
    ##cv.namedWindow(src_window)
    cv.namedWindow(dst_window)
    while True:
        ret,frame = video.read()
        if frame is None:
            break
        (success,boxes) = trackers.update(frame)
        for box in boxes:
            (x,y,w,h) = [int(a) for a in box]
            cv.rectangle(frame,(x,y),(x+w,y+h),(100,255,0),2)
        key = cv.waitKey(10)
        if key == ord('p'):
            cv.waitKey(-1)
        frame_HSV = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        frame_threshold = cv.inRange(frame_HSV,(low["H"],low["S"],low["V"]),(high["H"],high['S'],high["V"]))
        ##cv.imshow(src_window, frame)
        cv.imshow(dst_window, frame_threshold)
        cv.imshow(src_window, frame)
        if key == ord('q') or key == 27:
            break
    video.release()
    cv.destroyAllWindows()
          
if __name__ == "__main__":
    ## Add video path to the command
    ##video = sys.argv[1]
    cap = cv.VideoCapture(r'../footage/chipper.mp4')
    main(cap)