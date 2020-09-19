#!/usr/bin/python3
import os

#Controller: 	192.168.86.55
#Robot:		191.168.86.39

def controlToRobot():
	#send tx file to robots ram folder
	cmd  = 'scp /dev/shm/ctr pi@192.168.86.39:/dev/shm/'
	os.system(cmd)
	return

def robotToControl():
	cmd = 'scp /dev/shm/rtc pi@192.168.86.55:~/rx'
	os.system(cmd)
	return

def videoTX():
	cmd = 'scp /dev/shm/vid pi@192.168.86.39:/dev/shm/'
	os.system(cmd)
	return


if __name__ == '__main__':
	controlToRobot()
