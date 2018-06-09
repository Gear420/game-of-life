//
// Created by 张兴宇 on 2018/6/9.
//

#include <iostream>
#include <stdlib.h>
#include "graph.h"
#include <time.h>
using namespace std;

int main(){
    Graph *g = new Graph(20);
    g->print();
    cout<<"****************************"<<endl;
    g->change_status();
    g->print();

}

