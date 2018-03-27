# -*- coding:utf-8 -*-

from tkinter import *
from tkinter import ttk


def submitForm():
    print("Submit")
    button2.state(['disabled'])


def checkChanged():
    print("checkChanged %s" % measureSystem.get())

def selected(v):
    print("Selected %s" % country.get())

if __name__ == '__main__':
    root = Tk()
    root.geometry('640x480')
    root.title('Hello world')

    button = ttk.Button(root, text='Okay', command=submitForm)

    button.pack()

    button2 = ttk.Button(root, text='NO', command=submitForm)

    button2.pack()

    measureSystem = StringVar()
    check = ttk.Checkbutton(root, text='Use Metric',
                            command=checkChanged, variable=measureSystem,
                            onvalue='metric', offvalue='imperial')
    check.pack()

    phone = StringVar()
    home = ttk.Radiobutton(root, text='Home', variable=phone, value='home')
    office = ttk.Radiobutton(root, text='Office', variable=phone, value='office')
    cell = ttk.Radiobutton(root, text='Mobile', variable=phone, value='cell')
    home.pack()
    office.pack()
    cell.pack()

    username = StringVar()
    name = ttk.Entry(root, textvariable=username)
    name.pack()

    password = StringVar()
    pw = ttk.Entry(root, textvariable=password)
    pw.configure(show='*')
    pw.pack()

    countryvar = StringVar()
    country = ttk.Combobox(root, textvariable=countryvar)
    country['values'] = ('USA', 'Canada', 'Australia')
    country.bind('<<ComboboxSelected>>', selected)
    country.pack()

    root.mainloop()
