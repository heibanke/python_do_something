#!/usr/bin/env python
# -*- coding: utf-8 -*-
#copyRight by heibanke

import wx

# 每个wxPython的程序必须有一个wx.App对象.
#默认是False，True则将输出和错误重定向到窗口，False为控制台
app = wx.App(True)

frame = wx.Frame(None, -1, title='Hello World', pos=(300,400), size=(200,150))
#frame.Centre()
frame.Show()

print "heibanke is here"
print "Error here"

# 进入循环，等待响应
app.MainLoop()
