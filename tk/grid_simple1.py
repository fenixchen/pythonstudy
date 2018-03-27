'''2.使用row和column来指定位置'''
# -*- coding: utf-8 -*-
# 使用grid来布局组件
from tkinter import *

root = Tk()
# 创建两个Label
lb1 = Label(root, text='Hello')
lb2 = Label(root, text='Grid')

lb1.grid(row=0, column=0)
# 指定lb2为第一行（使用索引0开始），第二列（使用索引0开始）
lb2.grid(row=1, column=1)

root.mainloop()
# grid有两个最为重要的参数，用来指定将组件放置到什么位置，一个是row,另一个是column。如果不指定row,会将组件放置到第一个可用的行上，
# 如果不指定column，则使用第一列。注意这里使用grid时不需要创建，直接使用行列就可以。
