'''5.将两个或多个组件同一个位置'''
# -*- coding: utf-8 -*-
# 多个组件同时grid到同一个表格位置
from tkinter import *

root = Tk()
# 创建两个Label
lb1 = Label(root, text='1')
lb2 = Label(root, text='2')

# 将lb1和lb2均grid到(0,0)位置
lb1.grid(row=0, column=0)
lb2.grid(row=0, column=0)


def forgetLabel():
    # grid_slaves返回grid中(0,0)位置的所有组件
    # grid_forget将这个组件从grid中移除（并未删除，可以使用grid再将它显示出来)
    print(root.grid_slaves(0, 0)[0].grid_forget())


# 我测试时grid_salves返回的第一个值为lb2，最后grid的那一个
Button(root, text='forget last', command=forgetLabel).grid(row=1)

root.mainloop()
# 这段代码是用来证明，多个组件同时放置到同一个位置上会产生覆盖的问题。对于grid_slaves返回的组件list如何排序，
# 我没有去查想着资料，在这个例子中使用索引0，返回的正好是lb2,然后再使用grid_forget将这个删除从grid中移除，
# 可以看到lb1显示出来了。
