import sys
import os
import tkMessageBox
from Tkinter import *
from projectTory import *
from tkFileDialog import askopenfilename




def email(event):
	#output = Label(topFrame, text="Sending E-mail..." ).pack()
	one()
	tkMessageBox.showinfo("Alert", "E-mail Sent!")


def receive(event):
	#two()
    automator()
    tkMessageBox.showinfo("Error", "This feature is not yet enabled.")

def open_file():
    filePath = askopenfilename(filetypes = (("Numbers Documents","*.numbers"), ("All Files","*.*")))
    print(filePath)
    return filePath

def handle_file():
    filePath = open_file()


class MyFirstGUI:
    def __init__(self, master):
        self.master = master

        self.label = Label(master, text="This is my first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings")


root = Tk()
root.title("Minnie")
root.resizable(width=False, height=False)
root.iconbitmap('icon.ico')
root.configure(background="yellow")
bottomFrame = Frame(root)

bottomFrame.pack(side = BOTTOM)


w = 370 # width for the Tk root
h = 370 # height for the Tk root

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
#
#


left = Label(root, text="Sent Order E-mail List", bg = "green", width="20")
left.bind("<Button-1>", email)
left.pack(side = LEFT, fill=Y)
right = Label(root, text="Receive Parts", bg = "blue", width="20")
right.bind("<Button-1>", receive)
right.pack(side = RIGHT, fill=Y)


#order = Button(topFrame, text = "SEND ORDER E-MAIL LIST", bg = "blue", command = email)


setup = Button(bottomFrame, text = "Setup Directory", bg = "red", command = handle_file)
setup.pack(side = BOTTOM)

#order.pack()
#receive.pack()
#myWindow = Label(root, bg="yellow").pack()
#topFrame.pack()
root.mainloop()