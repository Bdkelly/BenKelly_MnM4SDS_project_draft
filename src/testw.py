import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../footage/gameimg.jpg')
height,width,channels = img.shape
src = np.float32([[0, height], [1274, height], [0, 0], [width, 0]])
dst = np.float32([[600, height], [700, height], [0, 0], [width, 0]])
m = cv2.getPerspectiveTransform(src,dst)
warped_img = cv2.warpPerspective(img,m,(height,width))
plt.imshow(cv2.cvtColor(warped_img, cv2.COLOR_BGR2RGB)) # Show results
plt.show()