# -*- coding:utf-8 -*-

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


def new_file():
    print("New File")


def open_file(*arg):
    print("Open File")


def center(window):
    window.update_idletasks()
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    size = tuple(int(_) for _ in window.geometry().split('+')[0].split('x'))
    x = w / 2 - size[0] / 2
    y = h / 2 - size[1] / 2
    window.geometry("%dx%d+%d+%d" % (size + (x, y)))


def About():
    toplevel = Toplevel(root)

    label1 = Label(toplevel, text="about", height=0, width=50)
    label1.pack()
    label2 = Label(toplevel, text="Hello", height=0, width=50)
    label2.pack()

    toplevel.focus_set()
    toplevel.grab_set()
    toplevel.transient(root)
    center(toplevel)
    toplevel.wait_window(toplevel)


def tree_selected(event):
    item = event.widget.selection()[0]
    item_text = event.widget.item(item, "text")
    status.set(item_text)


class StatusBar(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.label.pack(fill=X)

    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()


class ToolBar(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.button1 = Button(self, text='new', width=6, relief=GROOVE)
        self.button1.pack(side=LEFT, padx=2, pady=2)

        self.button2 = Button(self, text='open', width=6, relief=GROOVE)
        self.button2.pack(side=LEFT, padx=2, pady=2)


if __name__ == '__main__':
    root = Tk()
    root.title("Monitor OSD Designer")
    # root.geometry("800x600")
    menu = Menu(root, tearoff=0)
    root.config(menu=menu)

    file_menu = Menu(menu, tearoff=0)
    menu.add_cascade(label="File", menu=file_menu)

    file_menu.add_command(label="New", command=new_file, underline=0)

    file_menu.add_command(label="Open...",
                          command=open_file,
                          underline=1,
                          accelerator="Ctrl+O")
    root.bind_all("<Control-o>", open_file)

    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)

    help_menu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About...", command=About)

    frame = Frame(root, relief='sunken', borderwidth=1)
    frame.grid(sticky='nwse')

    toobar = ToolBar(frame)
    toobar.grid(row=0, column=0, columnspan=3, sticky=EW)

    tree = ttk.Treeview(frame, columns=('Type'))
    tree.heading('#0', text='Item')
    tree.heading('#1', text='')
    tree.column('#0', stretch=YES)

    icon_scene = ImageTk.PhotoImage(Image.open('scene.png'))
    icon_glyph = ImageTk.PhotoImage(Image.open('glyph.png'))
    icon_ingredient = ImageTk.PhotoImage(Image.open('ingredient.png'))
    icon_window = ImageTk.PhotoImage(Image.open('window.png'))

    scene = tree.insert('', 'end', 'scene', text='TVDemo', values=(''), image=icon_scene)
    glyph = tree.insert(scene, 'end', text='Glyphs', image=icon_glyph)
    ingredient = tree.insert(scene, 'end', text='Ingredients', image=icon_ingredient)
    window = tree.insert(scene, 'end', text='Windows', image=icon_window)

    tree.insert(glyph, 'end', text='A')
    tree.insert(glyph, 'end', text='B')
    tree.insert(glyph, 'end', text='C')

    tree.insert(ingredient, 'end', text='Line0', values=('(1,1)-(100,100)'))
    tree.insert(ingredient, 'end', text='Rectangle0')
    tree.insert(ingredient, 'end', text='Bitmap0')
    tree.insert(ingredient, 'end', text='Character0', values=('\'A\''))
    tree.insert(ingredient, 'end', text='Character1', values=('\'C\''))
    tree.insert(ingredient, 'end', text='Character2', values=('\'Z\''))

    tree.insert(window, 'end', text='Window0')
    tree.insert(window, 'end', text='Window1')
    tree.insert(window, 'end', text='Window2')

    tree.item(glyph, open=TRUE)
    tree.item(ingredient, open=TRUE)
    tree.item(window, open=TRUE)
    tree.item(scene, open=TRUE)

    ysb = ttk.Scrollbar(frame, orient='vertical', command=tree.yview)
    xsb = ttk.Scrollbar(frame, orient='horizontal', command=tree.xview)
    tree.configure(yscroll=ysb.set, xscroll=xsb.set)

    tree.bind('<<TreeviewSelect>>', tree_selected)

    tree.grid(row=1, column=0, sticky=NSEW)
    ysb.grid(row=1, column=1, sticky='ns')
    xsb.grid(row=2, column=0, sticky='ew')

    frame_right = Frame(frame, bd=1, relief=GROOVE)
    frame_right.grid(row=1, column=2, sticky=NSEW)

    title = Label(frame_right, text='Scene', relief=GROOVE)
    title.grid(columnspan=2, sticky=NSEW)

    for i in range(1, 20):  # Rows
        prop = Label(frame_right, text='Prop %d' % i, relief=FLAT, bg='#A0A0A0')
        value = Entry(frame_right)
        prop.grid(row = i, column=0, sticky=NSEW)
        value.grid(row=i, column=1, sticky=NSEW)

    frame_right.columnconfigure(0, weight=1)
    frame_right.columnconfigure(1, weight=2)

    status = StatusBar(frame)
    status.grid(row=3, column=0, columnspan=3, sticky=EW)

    frame.rowconfigure(1, weight=1)
    frame.columnconfigure(0, weight=3)
    frame.columnconfigure(2, weight=1)

    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    root.state('zoomed')

    # center(root)

    mainloop()
