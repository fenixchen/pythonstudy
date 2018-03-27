# -*- coding:utf-8 -*-


'''''Tkinter教程之Grid篇'''
# Tkinter参考中最推荐使用的一个布局器。
# 实现机制是将Widget逻辑上分割成表格，在指定的位置放置想要的Widget就可以了。
'''''1.第一个Grid例子'''
# -*- coding: utf-8 -*-
# 使用grid来布局组件

from tkinter import *

root = Tk()
# 创建两个Label

lb1 = Label(root, text='Hello')
lb2 = Label(root, text='Grid')

lb1.grid()
lb2.grid()

root.mainloop()

# grid有两个最为重要的参数，用来指定将组件放置到什么位置，一个是row,另一个是column。
# 如果不指定row,会将组件放置到第一个可用的行上，如果不指定column，则使用第一列。
