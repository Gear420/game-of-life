from graph import Graph
from draw import cellSet
from tkinter import *
import time

#
# def autoclose():
#

cellGraph = Graph(20)
root = Tk()
root.title("draw")
cellSet(cellGraph, root)
root.mainloop()
