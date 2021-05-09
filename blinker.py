from gpiozero import LED
from time import sleep
import tkinter.font
import RPi.GPIO as GPIO
from tkinter import *
GPIO.setmode(GPIO.BCM)


yellow = LED(18)
red = LED(22)
blue = LED(27)

                                             


window = Tk()
window.title("TOGGLE LED")
myFont = tkinter.font.Font(family = 'Calibri', size = 10, weight = "bold")


def toggleblue():
    if blue.is_lit:
        blue.off()
        blueButton["text"] = "Turn B LED on"
    else:
        blue.on()
        blueButton["text"] = "Turn B LED off"

def toggleyellow():
    if yellow.is_lit:
        yellow.off()
        yellowButton["text"] = "Turn Y LED on"
    else:
        yellow.on()
        yellowButton["text"] = "Turn Y LED off"
        
def togglered():
    if red.is_lit:
        red.off()
        redButton["text"] = "Turn R lED on"
    else:
        red.on()
        redButton["text"] = "Turn R LED off"





blueButton = Button(window, text = 'Turn B LED On', font = myFont, command = toggleblue, bg = 'blue', height = 2, width = 14)
blueButton.grid(row=3,column=3)

redButton = Button(window, text = 'Turn R LED On', font = myFont, command = togglered, bg = 'red', height = 2, width = 14)
redButton.grid(row=1,column=1)

yellowButton = Button(window, text = 'Turn Y LED On', font = myFont, command = toggleyellow, bg = 'yellow', height = 2, width = 14)
yellowButton.grid(row=2,column=2)