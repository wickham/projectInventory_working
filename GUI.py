import sys
import os
import tkMessageBox
from Tkinter import *
from projectTory import *
import tkFileDialog




def email(event):
	#output = Label(topFrame, text="Sending E-mail..." ).pack()
	one()
	tkMessageBox.showinfo("Alert", "E-mail Sent!")


def csvExport(event):
    #two()
    automator()
    tkMessageBox.showinfo("Complete", "Export Completed!")


class set_dir:
    def __init__(self):
        return    
    #@staticmethod
    def root(self):
        curdir = os.getcwd()
        filePath = tkFileDialog.askdirectory(parent = root, initialdir = curdir, title = "Select Directory")
        folder = Folder(filePath)
        folder.set(filePath, "root")      
    #@staticmethod
    def results(self):
        curdir = os.getcwd()
        filePath = tkFileDialog.askdirectory(parent = root, initialdir = curdir, title = "Select Directory")
        folder = Folder(filePath)
        folder.set(filePath, "results")

        


def handle_file():
    filePath = open_file()

def browse():
    filePath = tkFileDialog.askopenfilename(filetypes = (("Numbers Documents","*.numbers"), ("All Files","*.*")))
    setDatabase(filePath, "numbersDoc")


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
right = Label(root, text="Generate Export Files", bg = "blue", width="20")
right.bind("<Button-1>", csvExport)
right.pack(side = RIGHT, fill=Y)


#order = Button(topFrame, text = "SEND ORDER E-MAIL LIST", bg = "blue", command = email)

Set_dir = set_dir()
root = Button(bottomFrame, text = "Select App Directory", bg = "red", command =Set_dir.root)
root.pack(side = BOTTOM)
setup = Button(bottomFrame, text = "Select .csv Folder", bg = "red", command = Set_dir.results)
setup.pack(side = BOTTOM)
data = Button(bottomFrame, text = "Select Database.numbers", command = browse)
data.pack(side = BOTTOM)



#order.pack()
#receive.pack()
#myWindow = Label(root, bg="yellow").pack()
#topFrame.pack()
root.mainloop()