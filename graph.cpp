//
// Created by 张兴宇 on 2018/6/9.
//

#include"graph.h"


Graph::Graph(int size) {
    this->size = size;
    srand((unsigned)time(NULL));
    for(int i =0 ;i<this->size;i++) {
        vector<int> a;
        vector<int> b;
        for (int j = 0; j < this->size; j++) {
            a.push_back(rand() % 2);
            b.push_back(0);
        }
        graph.push_back(a);
        graph_status.push_back(b);
    }
}
void Graph::count_neighbour() {

    for(int i =0 ;i<size;i++)
    {
        for(int j =0 ;j<size;j++)
        {
            int cnt = 0;
            for(int ii = -1 ;ii<=1;ii++)
            {
                if(i+ii<0||i+ii>=size)
                    continue;
                for(int jj=-1 ;jj<=1;jj++)
                {
                    if(j+jj<0||j+jj>=size)
                        continue;
                    if(ii==i&&jj==j)
                        continue;
                    if(graph[i+ii][j+jj]==1)
                        cnt++;
                }
            }
            if(cnt==2)
            {
                graph_status[i][j]=graph[i][j];
            }
            else if(cnt==3)
            {
                graph_status[i][j] = 1;
            }
            else
                graph_status[i][j] = 0;
        }
    }
}

void Graph::change_status() {


    count_neighbour();
    for(int i = 0; i<size ;i++)
    {
        for(int j =0 ;j<size ;j++)
        {
            graph[i][j] = graph_status[i][j];
        }
    }
}