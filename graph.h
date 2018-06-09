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
    //vector<vector<int> > graph_status;
public:
    Graph(int size){
        this->size = size;
        srand((unsigned)time(NULL));
        for(int i =0 ;i<this->size;i++) {
            vector<int> a;
            for (int j = 0; j < this->size; j++) {
                a.push_back(rand() % 2);
            }
            graph.push_back(a);
        }

    }
    void print(){
        for(int i =0 ;i<this->size;i++)
        {
            for(int j =0; j<this->size;j++)
            {
                cout << graph[i][j] << ' ';
            }
            cout << endl;
        }
    }


};

#endif //GAME_OF_LIFE_GRAPH_H
