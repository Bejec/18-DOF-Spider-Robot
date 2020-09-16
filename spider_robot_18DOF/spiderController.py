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

master = tk.Tk()
master.title("GPIO Control")
master.geometry("800x450") #800x480
master.configure(background='black')

# https://stackoverflow.com/questions/23901168/how-do-i-insert-a-jpeg-image-into-a-python-tkinter-window
path = "/home/pi/testScreen.png"

imgsmall = Image.open(path)
new_image = imgsmall.resize((400,240))
new_image.save("/home/pi/testScreenSmall.png")
newpath = "/home/pi/testScreenSmall.png"
img = ImageTk.PhotoImage(Image.open(newpath))
panel = tk.Label(master, image = img)
panel.grid(row=1, column=2, columnspan=5, rowspan=3)

GPIO21_state = True
GPIO20_State = True

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

ONbutton = tk.Button(master, text="Plane Move", bg="blue", command=GPIO21button)
ONbutton.grid(row=0, column=0, columnspan=2, rowspan=2)

OFFbutton = tk.Button(master, text="Body Pan",bg="blue" , command=GPIO20button)
OFFbutton.grid(row=2, column=0, columnspan=2, rowspan=2)

notifications = tk.Button(master, text="Notifications", bg="blue", command=GPIO21button)
notifications.grid(row=0, column=2, columnspan=5)

function1 = tk.Button(master, text="func1", bg="blue", command=GPIO21button)
function1.grid(row=4, column=0, columnspan=3, rowspan=2)

povScreen = tk.Button(master, text="Virtual 3rd POV", bg="blue", command=GPIO21button)
povScreen.grid(row=4, column=3, columnspan=3, rowspan=2)

termOut = tk.Button(master, text="Terminal Out", bg="blue", command=GPIO21button)
termOut.grid(row=4, rowspan=2, column=6, columnspan=2)

rssiC = tk.Button(master, text="RSSI C", bg="blue", command=GPIO21button)
rssiC.grid(row=0, column=8)

rssiR = tk.Button(master, text="RSSI R", bg="blue", command=GPIO21button)
rssiR.grid(row=0, column=9)

rotateSlider = tk.Button(master, text="Rotate Slider", bg="blue", command=GPIO21button)
rotateSlider.grid(row=1, column=8, columnspan=2)

heightSlider = tk.Button(master, text="Height Slider", bg="blue", command=GPIO21button)
heightSlider.grid(row=2, column=8, columnspan=2)

function2 = tk.Button(master, text="functions 2", bg="blue", command=GPIO21button)
function2.grid(row=4, rowspan=2, column=8, columnspan=2)




Exitbutton = tk.Button(master, text="Exit",bg="red", command=master.destroy)
Exitbutton.grid(row=5, column=9)
master.mainloop()