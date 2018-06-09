from graph import Graph
from draw import cellSet
from tkinter import *
import time

cellGraph = Graph(20)
for t in range(100):
    root = Tk()
    root.title("draw")
    g = cellGraph.cell_g()
    print(g)
    app = cellSet(g,root)
    root.mainloop()
    cellGraph.chanege_status()
    root.quit()