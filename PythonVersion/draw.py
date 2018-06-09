from tkinter import *
from graph import Graph
import time


class cellSet(Frame):
    def __init__(self,cellGraph,master):
        self.root = master  # 定义内部变量root
        Frame.__init__(self, master)
        self.root.geometry('%dx%d' % (400,400))  # 设置窗口大小
        self.cellGraph = cellGraph
        self.updateUI()
        print("now quit!")
        #self.destroy()
        # self.closewindow()

    def updateUI(self):
        g = self.cellGraph.cell_g()
        for i in range(20):
            for j in range(20):
                if g[i][j] == 1:
                    self.create(i, j)
                if g[i][j] == 0:
                    self.delete(i,j)
        self.cellGraph.chanege_status()
        self.after(1000, self.updateUI)


    def create(self,x,y):
        self.cell = Frame(self.root, width=20, height=20, bg="red")
        self.cell.place(x=x*20,y = y*20,width = 20,height =20 )

    def delete(self, x, y):
        self.cell = Frame(self.root, width=20, height=20, bg="white")
        self.cell.place(x=x * 20, y=y * 20, width=20, height=20)
    # def closewindow(self):
    #     # time.sleep(10)
    #     self.root.quit()
