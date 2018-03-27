# -*- coding:utf-8 -*-

from tkinter import *
from tkinter import ttk

if __name__ == '__main__':
    root = Tk()
    root.geometry('640x480')
    root.title('Hello world')

    label = ttk.Label(root, text='Full name:')

    label.pack()

    var = StringVar()
    label['textvariable'] = var

    var.set("Hello world")
    root.mainloop()
