import glob
import cv2

videos = glob.glob('/path/to/videos/*.mp4')
fl=0
for v in videos:
  print "Screening:",v
  cap = cv2.VideoCapture(v)
  ctr = 0
  frames = cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)
  while ctr<=frames:
    cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES,ctr)
    ret,im = cap.read()
    cv2.imwrite("/path/to/store/snaps/"+str(fl)+"_"+str(ctr/30)+".jpg",im)
    ctr+=30
  fl+=1
  cap.release()
