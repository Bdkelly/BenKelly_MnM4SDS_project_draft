import cv2
import numpy

def main(video):
    track_xl = cv2.MultiTracker_create()
    container = build(track_xl,video)
    merge(container,video)

def build(track_xl,video,num=6):
    tri_dic = {'csrt':cv2.TrackerCSRT_create,'kcf':cv2.TrackerKCF_create,
                'boosting' : cv2.TrackerBoosting_create,'mil': cv2.TrackerMIL_create}
    ret, frame = video.read()
    for i in range(num):
        cv2.imshow("Frame",frame)
        rec = cv2.selectROI("Frame",frame)
        track = tri_dic["csrt"]()
        track_xl.add(track,frame,rec)
    return track_xl

def merge(trackers,video):
    while True:
        ret, frame = video.read()
        if not ret:
            break
        (success,boxes) = trackers.update(frame)
        for box in boxes:
            (x,y,w,h) = [int(a) for a in box]
            cv2.rectangle(frame,(x,y),(x+w,y+h),(100,255,0),2)
        cv2.imshow("Frame",frame)
        key = cv2.waitKey(5) & 0xFF
        if key == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video = cv2.VideoCapture(r'../footage/chipper.mp4') 
    main(video)
    ##justvid(video)