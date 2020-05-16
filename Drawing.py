#coding=utf-8
"""
    简单的画图软件
"""
from tkinter import *
from tkinter import messagebox
from tkinter.colorchooser import *
from tkinter.dialog import *
import random

win_width = 600
win_height = 450
bgcolor = "#ffffff"
fgcolor = "#ff0000"

color = ["#ff0000", "#00ff00", "#0000ff"]

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.creatWidget()
        self.startdrawflag = False
        self.x = 0
        self.y = 0
        self.last = 0

    def creatWidget(self):
        self.drawpad = Canvas(root, width=win_width, height=win_height*0.9, bg=bgcolor)
        self.drawpad.pack()
        self.but_pen = Button(root, text="画笔", name="pen")
        self.but_pen.pack(side="left")
        self.but_pen = Button(root, text="直线", name="line")
        self.but_pen.pack(side="left")
        self.but_rectangle = Button(root, text="矩形", name="rectangle")
        self.but_rectangle.pack(side="left")
        self.but_circle = Button(root, text="椭圆", name="circle")
        self.but_circle.pack(side="left")
        self.but_arrow = Button(root, text="箭头", name="arrow")
        self.but_arrow.pack(side="left")
        self.but_eraser = Button(root, text="橡皮", name="eraser")
        self.but_eraser.pack(side="left")
        self.but_clear = Button(root, text="清屏", name="clear")
        self.but_clear.pack(side="left")

        self.but_colorful_pen = Button(root, text="彩笔", name="colorful_pen")
        self.but_colorful_pen.pack(side="left")

        # 绑定事件
        self.but_eraser.bind_class("Button", "<1>", self.eventSolve)
        self.drawpad.bind("<ButtonRelease-1>", self.over_draw)

    def eventSolve(self, event):
        """按钮事件绑定"""
        name = event.widget.winfo_name()
        print(name)

        if name == "pen":
            self.drawpad.bind("<B1-Motion>", self.mypen)
        elif name == "line":
            self.drawpad.bind("<B1-Motion>", self.myline)
        elif name == "rectangle":
            self.drawpad.bind("<B1-Motion>", self.myrectangle)
        elif name == "circle":
            self.drawpad.bind("<B1-Motion>", self.mycircle)
        elif name == "arrow":
            self.drawpad.bind("<B1-Motion>", self.myarrow)
        elif name == "eraser":
            self.drawpad.bind("<B1-Motion>", self.myeraser)
        elif name == "clear":
            # self.drawpad.bind("<B1-Motion>", self.myclear)---- 不好使
            self.drawpad.delete("all")
        elif name == "colorful_pen":
            self.drawpad.bind("<B1-Motion>", self.mycolorful_pen)

    # 按钮事件处理
    def start_draw(self, event):
        """绘画准备"""
        self.drawpad.delete(self.last)
        if not self.startdrawflag:
            self.x = event.x
            self.y = event.y
            self.startdrawflag = True

    def over_draw(self, event):
        """绘画结束"""
        self.startdrawflag = False
        self.last = 0

    def mypen(self, event):
        self.start_draw(event)
        self.last = self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=fgcolor)
        print("x:" + str(event.x) + "    y:" + str(event.y))
        self.x = event.x
        self.y = event.y
        self.last = 0

    def myline(self, event):
        self.start_draw(event)
        self.last = self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=fgcolor)

    def myrectangle(self, event):
        self.start_draw(event)
        self.last = self.drawpad.create_rectangle(self.x, self.y, event.x, event.y, outline=fgcolor)

    def mycircle(self, event):
        self.start_draw(event)
        self.last = self.drawpad.create_oval(self.x, self.y, event.x, event.y, fill=fgcolor)

    def myarrow(self, event):
        self.start_draw(event)
        self.last = self.drawpad.create_line(self.x, self.y, event.x, event.y, arrow=LAST, fill=fgcolor)

    def myeraser(self, event):
        self.start_draw(event)
        self.last = self.drawpad.create_oval(event.x-4, self.y-4, event.x+4, event.y+4, fill=bgcolor, outline=bgcolor)
        print("x:"+str(event.x)+"    y:"+str(event.y))
        self.x = event.x
        self.y = event.y
        self.last = 0

    def myclear(self, event):
        self.drawpad.delete("all")

    def mycolorful_pen(self, event):
        self.start_draw(event)
        i = random.randrange(3)
        self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=color[i])
        print("x:" + str(event.x) + "    y:" + str(event.y))
        self.x = event.x
        self.y = event.y


if __name__ == "__main__":
    root = Tk()
    root.title("画图")
    root.geometry(str(win_width)+"x"+str(win_height)+"+200+100")
    app = Application(root)
    root.mainloop()
