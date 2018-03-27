'''6.改变列（行）的属性值'''
# -*- coding: utf-8 -*-
# 设置column的属性(columnconfigure)
from tkinter import *

root = Tk()
# 创建两个Label
lb1 = Label(root, text='1', bg='red')
lb2 = Label(root, text='2', bg='blue')

# 将lb1和lb2分别放置到第1行的1,2列位置上
lb1.grid(row=0, column=0)
lb2.grid(row=0, column=1)

# 指定列的最小宽度为100
root.columnconfigure(0, minsize=100)
root.mainloop()
# 1与2的距离变的远一些了。
# 但如果这个位置没有组件存在的话这个值是不起作用的.
# 设置列或行(rowconfigure)的属性时使用父容器的方法,不是自己调用。
