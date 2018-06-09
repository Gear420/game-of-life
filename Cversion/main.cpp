//
// Created by 张兴宇 on 2018/6/9.
//

#include <iostream>
#include "graph.h"
#include <unistd.h>
#include <stdlib.h>
using namespace std;

int main(){
    int size;//图形大小
    cout << "请输入图形大小 ：";
    cin>>size;
    char f ;
    cout<<"是否手动输入Y/N :";
    cin>>f;
    Graph *g;
    if(f=='Y')
    {
        cout<<"输入0/1"<<endl;
        g = new Graph(size,f);
    }
    else
        g = new Graph(size);

    while(1)
    {
        g->print();
        g->change_status();
        sleep(1);
        system("clear");
    }


}

