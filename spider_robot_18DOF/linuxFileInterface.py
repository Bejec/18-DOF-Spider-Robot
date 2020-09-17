#!/usr/bin/python3

def updateWifiStrength():
	path= '/proc/net/wireless'
	
	contents = open(path, 'r')
	
	contents = contents.read().split() #split at spaces
	#print("debug")
	#print (contents[29].strip('.'))
	#print("debug")
	return contents[29].strip('.')

if __name__ == "__main__":
	updateWifiStrength()

