from tkinter import *
from graph import Graph
import time


class cellSet(Frame):
    def __init__(self,g,master=None):
        self.root = master  # 定义内部变量root
        super().__init__(master)
        self.root.geometry('%dx%d' % (400,400))  # 设置窗口大小
        for i in range(20):
            for j in range(20):
                if g[i][j] == 1:
                    self.create(i,j)
        #self.dele()

    def create(self,x,y):
        self.cell = Frame(self.root, width=20, height=20, bg="red")
        self.cell.place(x=x*20,y = y*20,width = 20,height =20 )
    def dele(self):
        self.quit()
