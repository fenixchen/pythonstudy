# -*- coding:utf-8 -*-


from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename


def NewFile():
    print
    "New File!"


def OpenFile():
    name = askopenfilename()
    print
    name


def About():
    print
    "This is a simple example of a menu"


root = Tk()
menu = Menu(root)


root.config(menu=menu)

filemenu = Menu(menu)

filemenu['tearoff'] = 0

menu.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)

menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

mainloop()
