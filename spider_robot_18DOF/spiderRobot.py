#!/usr/bin/python3
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
import numpy as np
#import cv2
import threading
import time
import os

#def hello(*args):
#	print(str(args[0])+" It's "+str(time.ctime()))
#	next=int(args[0])+1
#	threading.Timer(0.001, hello,[str(next)]).start()

#hello("1")

def txrssir():
	path = '/proc/net/wireless'
	contents = open(path, 'r')
	contents = contents.read().split()
	print(contents)
	print('test')
	data = '1'
	try:
		print(contents[29])
	except:
		print('not connected yet')
	else:
		data = contents[29].strip('.') 
	print(data)
	#i might have to add \n after data[0] if i am writing a data[1]
	rtc = open('/dev/shm/rtc', 'w')
	rtc.writelines(data)
	rtc.close()
	cmd = 'scp -i /home/pi/.ssh/id_rsa /dev/shm/rtc pi@192.168.86.55:~/rx'
	try:
		os.system(cmd)
	except:
		print('no rtc file yet')
	t = threading.Timer(1, txrssir)
	t.start()

txrssir()

#cap = cv2.VideoCapture(0)

#while(True):
    # Capture frame-by-frame
 #   ret, frame = cap.read()

    # Our operations on the frame come here
  #  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
   # imwrite("/run/shm",frame);
	# cv2.imshow('frame',gray)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
        #break

# When everything done, release the capture
#cap.release()
#cv2.destroyAllWindows()
