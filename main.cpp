//
// Created by 张兴宇 on 2018/6/9.
//

#include <iostream>
#include "graph.h"
#include <unistd.h>
#include <stdlib.h>
using namespace std;

int main(){
    Graph *g = new Graph(10);
    int t=100;
    while(t--)
    {
        g->print();
        g->change_status();
        sleep(1);
        system("clear");
    }


}

