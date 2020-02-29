import cv2
import subprocess as sp
import numpy

#IMG_W = 1920
#IMG_H = 1080
IMG_W = 640
IMG_H = 480
size = (IMG_W,IMG_H)
# This image size is set in Android IP Webcam App
ffmpeg_cmd = [ 'ffmpeg',
			'-i', 'http://192.168.43.1:7000/videofeed',		#'-i', 'D:/Deploy.mp4',
			'-r', '10',					# FPS
			'-pix_fmt', 'bgr24',      	# opencv requires bgr24 pixel format.
			'-vcodec', 'rawvideo',
			'-an','-sn',                # disable audio processing
			'-vf', "select='eq(pict_type\,PICT_TYPE_I)'", 
			'-f', 'image2pipe', '-']    
pipe = sp.Popen(ffmpeg_cmd, stdout = sp.PIPE, bufsize=10)

i = 0
j = 0
out = cv2.VideoWriter(str(j) + '.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

while True:
	raw_image = pipe.stdout.read(IMG_W*IMG_H*3)
	image =  numpy.fromstring(raw_image, dtype='uint8')		# convert read bytes to np
	image = image.reshape((IMG_H,IMG_W,3))
	out.write(image)

	i = (i+1)%100
	if(i==0):
		out.release()
		j = j + 1
		out = cv2.VideoWriter(str(j) + '.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

	cv2.imshow('Video', image)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

pipe.stdout.flush()
cv2.destroyAllWindows()