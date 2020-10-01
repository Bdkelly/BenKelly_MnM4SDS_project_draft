import cv2
import numpy
import time

def main(tracker,video,num=1):
    while (video.isOpened()):
        ret, frame = video.read()
        rec = cv2.selectROI("MultiTracker",frame)
        tracker.init(frame,rec)
        if not ret:
            break
        (success,box) = tracker.update(frame)
        if success:
            (x,y,w,h) = [int(a) for a in box]
            cv2.rectangle(frame,(x,y),(x+w,y+h),(100,255,0),2)
        cv2.imshow("Frame",frame)
        key = cv2.waitKey(0) & 0xFF
        if key == ord('q'):
            break
    v.release()
    cv2.destroyAllWindows()

def justvid(video):
    while True:
        ret,frame = video.read()
        cv2.imshow("Frame",frame)
        if not ret:
            break
        cv2.imshow("Frame",frame)
        key = cv2.waitKey(0) & 0xFF
        if key == ord('q'):
            break
        cv2.destroyAllWindows()
    return


if __name__ == "__main__":
    tri_dic = {'csrt':cv2.TrackerCSRT_create,
               'kcf':cv2.TrackerKCF_create,
               'boosting' : cv2.TrackerBoosting_create,
               'mil': cv2.TrackerMIL_create}
    tracker = tri_dic["csrt"]()
    video = cv2.VideoCapture(r'footage/chipper.mp4') 
    main(tracker,video)
    ##justvid(video)