import cv2
import subprocess as sp
import numpy

IMG_W = 640
IMG_H = 480

ffmpeg_cmd = [ 'ffmpeg',
			'-i', 'http://192.168.0.100:7000/videofeed',
			'-r', '1',					# FPS
			'-pix_fmt', 'bgr24',      	# opencv requires bgr24 pixel format.
			'-vcodec', 'rawvideo',
			'-an','-sn', 
			'-vf', 'scale=640x480',             	# disable audio processing
			'-f', 'image2pipe', '-']    
pipe = sp.Popen(ffmpeg_cmd, stdout = sp.PIPE, bufsize=10**8)

while True:
	raw_image = pipe.stdout.read(IMG_W*IMG_H*3)
	image =  numpy.fromstring(raw_image, dtype='uint8')		# convert read bytes to np
	image = image.reshape((IMG_H,IMG_W,3))

	cv2.imshow('Video', image)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

pipe.stdout.flush()
cv2.destroyAllWindows()