from tkinter import *
from graph import Graph
import time


class cellSet(Frame):
    def __init__(self,cellGraph,size,master):
        self.root = master  # 定义内部变量root
        self.size = size
        Frame.__init__(self, master)
        self.root.geometry('%dx%d' % (size*10,size*10))  # 设置窗口大小
        self.cellGraph = cellGraph
        self.updateUI()
        #print("now quit!")
        #self.destroy()
        # self.closewindow()

    def updateUI(self):
        g = self.cellGraph.cell_g()
        for i in range(self.size):
            for j in range(self.size):
                if g[i][j] == 1:
                    self.create(i, j)
                if g[i][j] == 0:
                    self.delete(i,j)
        self.cellGraph.chanege_status()
        self.after(1000, self.updateUI)


    def create(self,x,y):
        self.cell = Frame(self.root, width=10, height=10, bg="black")
        self.cell.place(x=x*10,y = y*10,width = 10,height =10 )

    def delete(self, x, y):
        self.cell = Frame(self.root, width=10, height=10, bg="white")
        self.cell.place(x=x * 10, y=y * 10, width=10, height=10)
    # def closewindow(self):
    #     # time.sleep(10)
    #     self.root.quit()
