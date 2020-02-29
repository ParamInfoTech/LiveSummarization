# Using Android IP Webcam video .jpg stream (tested) in Python2 OpenCV3
import urllib.request as ur
import cv2
import numpy as np
import time

# Replace the URL with your own IPwebcam shot.jpg IP:port
url='http://192.168.0.100:7000/videofeed'

cap = cv2.VideoCapture(url)

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

#ffmpeg -i "http://192.168.0.100:7000/videofeed"
# -f image2 -vf "select='eq(pict_type,PICT_TYPE_I)'" -vsync vfr yi%03d.png