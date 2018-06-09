from graph import Graph
from draw import cellSet
from tkinter import *
import time

#
# def autoclose():
#
size = input("请输入size大小:")
size =(int)(size)
cellGraph = Graph(size)
root = Tk()
root.title("draw")
cellSet(cellGraph,size,root)
root.mainloop()
