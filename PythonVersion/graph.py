import os
from random import randint

class Graph:
    def __init__(self,size):
        self.size = size
        self.graph =[]
        self.graph_status =[]
        for i in range(size):
            a=[]
            b=[]
            for j in range(size):
                a.append(randint(1,100) % 2)
                b.append(0)
            self.graph.append(a)
            self.graph_status.append(b)

    def chanege_status(self):
        for i in range(self.size):
            for j in range(self.size):
                cnt = 0;
                for ii in range(-1,2):
                    if i+ii < 0 or i+ii >= self.size:
                        continue
                    for jj in range(-1,2):
                        if j + jj < 0 or j + jj >= self.size:
                            continue
                        if ii + i == i and jj + j == j:
                            continue
                        if self.graph[i + ii][j + jj] == 1:
                            cnt  = cnt+1
                if cnt == 2:
                    self.graph_status[i][j]=self.graph[i][j]
                elif cnt == 3:
                    self.graph_status[i][j] = 1
                else:
                    self.graph_status[i][j] = 0

        for i in range(self.size):
            for j in range(self.size):
                self.graph[i][j] = self.graph_status[i][j];

    def printg(self):
        for i in range(self.size):
            print(self.graph[i])
    def cell_g(self):
        return self.graph
