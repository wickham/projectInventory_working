import sys
import os
import tkMessageBox
from Tkinter import *
from projectTory import *



def email():
	one()
	tkMessageBox.showinfo("Alert", "E-mail Sent!")

def receive():
	two()
	tkMessageBox.showinfo("Error", "This feature is not yet enabled.")

root = Tk()

root.iconbitmap(r'/Users/Allen/Desktop/Current Work/CODE/projectInventory_working/images/check.png')
w = 200 # width for the Tk root
h = 100 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

# defining the framing of GUI
topFrame = Frame(root)
topFrame.pack()
frame = Frame(root, width = 300, height = 500)

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)



order = Button(topFrame, text = "SEND ORDER E-MAIL LIST", bg = "blue", command = email)

receive = Button(bottomFrame, text = "RECEIVE PARTS", fg = "red", command = receive)

order.pack()
receive.pack()

root.mainloop()