'''''4.将组件放置到预定位置上去'''
# -*- coding: utf-8 -*-
# 使用grid来布局组件
from tkinter import *

root = Tk()
# 创建两个Label
Label(root, text='1').grid()
# 在第1行，第11列放置lb2
Label(root, text='2').grid(row=0, column=10)
Label(root, text='3').grid(row=0, column=5)
root.mainloop()
# 可以看到Label('3')是位置Label('1')和Label('2')之间了，即Label('2')是在11列，Label('3')位于第3列