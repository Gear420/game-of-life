//
// Created by 张兴宇 on 2018/6/9.
//

#ifndef GAME_OF_LIFE_GRAPH_H
#define GAME_OF_LIFE_GRAPH_H

#include <vector>
#include<stdlib.h>
#include <iostream>
using namespace std;

class Graph{
private:
    int size;
    vector<vector<int> > graph;
    //int graph[][];
    vector<vector<int> > graph_status;
public:
    Graph(int size);
    Graph(int size, char f);
    void count_neighbour();
    void change_status();
    void print();
};

#endif //GAME_OF_LIFE_GRAPH_H
