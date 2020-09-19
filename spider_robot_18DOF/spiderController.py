#!/usr/bin/python3

import tkinter as tk
import RPi.GPIO as GPIO
from time import sleep
from PIL import ImageTk, Image

GPIO21 = 21
GPIO20 = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO21, GPIO.OUT)
GPIO.setup(GPIO20, GPIO.OUT)

#master = tk.Tk()
#master.title("GPIO Control")
#master.geometry("800x450") #800x480
#master.configure(background='black')

# https://stackoverflow.com/questions/23901168/how-do-i-insert-a-jpeg-image-into-a-python-tkinter-window
#path = "/home/pi/testScreen.png"
#
#imgsmall = Image.open(path)
#new_image = imgsmall.resize((400,240))
#new_image.save("/home/pi/testScreenSmall.png")
#newpath = "/home/pi/testScreenSmall.png"
#img = ImageTk.PhotoImage(Image.open(newpath))
#panel = tk.Label(master, image = img)
#panel.grid(row=1, column=2, columnspan=5, rowspan=3)

GPIO21_state = True
GPIO20_State = True

class main():
	def __init__(self):
		self.master = tk.Tk()
		self.master.title("GPIO Control")
		self.master.geometry("800x450") #800x480
		self.master.configure(background='black')

		# https://stackoverflow.com/questions/23901168/how-do-i-insert-a-jpeg-image-into-a-python-tkinter-window
		self.path = "/home/pi/testScreen.png"

		self.imgsmall = Image.open(self.path)
		self.new_image = self.imgsmall.resize((400,240))
		self.new_image.save("/home/pi/testScreenSmall.png")
		self.newpath = "/home/pi/testScreenSmall.png"
		self.img = ImageTk.PhotoImage(Image.open(self.newpath))
		self.panel = tk.Label(self.master, image = self.img)
		self.panel.grid(row=1, column=2, columnspan=5, rowspan=3)

		self.ONbutton = tk.Button(self.master, text="Plane Move", bg="blue", command=self.GPIO21button)
		self.ONbutton.grid(row=0, column=0, columnspan=2, rowspan=2)

		self.OFFbutton = tk.Button(self.master, text="Body Pan",bg="blue" , command=self.GPIO20button)
		self.OFFbutton.grid(row=2, column=0, columnspan=2, rowspan=2)

		self.notifications = tk.Button(self.master, text="Notifications", bg="blue", command=self.GPIO21button)
		self.notifications.grid(row=0, column=2, columnspan=5)

		self.function1 = tk.Button(self.master, text="func1", bg="blue", command=self.GPIO21button)
		self.function1.grid(row=4, column=0, columnspan=3, rowspan=2)

		self.povScreen = tk.Button(self.master, text="Virtual 3rd POV", bg="blue", command=self.GPIO21button)
		self.povScreen.grid(row=4, column=3, columnspan=3, rowspan=2)

		self.termOut = tk.Button(self.master, text="Terminal Out", bg="blue", command=self.GPIO21button)
		self.termOut.grid(row=4, rowspan=2, column=6, columnspan=2)

		self.rssiC = tk.Button(self.master, text="RSSI C", bg="black", fg="white", command=self.GPIO21button)
		self.rssiC.grid(row=0, column=8)

		self.rssiR = tk.Button(self.master, text="RSSI R", bg="black", fg="white", command=self.GPIO21button)
		self.rssiR.grid(row=0, column=9)

		self.rotateSlider = tk.Button(self.master, text="Rotate Slider", bg="blue", command=self.GPIO21button)
		self.rotateSlider.grid(row=1, column=8, columnspan=2)

		self.heightSlider = tk.Button(self.master, text="Height Slider", bg="blue", command=self.GPIO21button)
		self.heightSlider.grid(row=2, column=8, columnspan=2)

		self.function2 = tk.Button(self.master, text="functions 2", bg="blue", command=self.GPIO21button)
		self.function2.grid(row=4, rowspan=2, column=8, columnspan=2)

		self.Exitbutton = tk.Button(self.master, text="Exit",bg="red", command=self.master.destroy)
		self.Exitbutton.grid(row=5, column=9)

		self.master.after(0, self.update_RSSIC)
		self.master.after(0, self.update_RSSIR)

		self.master.mainloop() #should be last line of this definition


	def update_RSSIC(self):
		path = '/proc/net/wireless'
		contents = open(path, 'r')
		contents = contents.read().split() #split at spaces
		RSSIC = 'RSSI C: ' + contents[29].strip('.')
		#print (RSSIC)
		self.rssiC.configure(text = RSSIC)
		self.rssiC.after(500, self.update_RSSIC)


	def update_RSSIR(self):
		path = '/home/pi/rx/rtc'
		data = open(path, 'r')
		data = data.read()
		RSSIR = 'RSSI R: ' + data
		self.rssiR.configure(text = RSSIR)
		self.rssiR.after(500, self.update_RSSIR)


	def GPIO21button():
		global GPIO21_state
		if GPIO21_state == True:
			GPIO.output(GPIO21, GPIO21_state)
			GPIO21_state = True
			ONlabel = tk.Label(master, text="Turned ON", fg="green")
			ONlabel.grid(row=0, column=1)
		else:
			GPIO.output(GPIO21, GPIO21_state)
			GPIO21_state = True
			ONlabel = tk.Label(master, text="Turned OFF", fg="red")
			ONlabel.grid(row=0, column=1)


	def GPIO20button():
		global GPIO20_State
		if GPIO20_State == True:
			GPIO.output(GPIO20, GPIO20_State)
			GPIO20_State = True
			OFFlabel = tk.Label(master, text="Turned ON", fg="green")
			OFFlabel.grid(row=1, column=1)
		else:
			GPIO.output(GPIO20, GPIO20_State)
			GPIO20_State = True
			OFFlabel = tk.Label(master, text="Turned OFF", fg="red")
			OFFlabel.grid(row=1, column=1)

app = main()
