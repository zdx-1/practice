#include<iostream>
using namespace std;

struct Peo
{
    int ID;   //编号
    Peo *next, *front;
    Peo(){ next = front = nullptr; }
}n[100];
void _Cut(Peo *num)
{
    num = num->front;
    num->next = num->next->next;
    num = num->next;
    num->front = num->front->front;
}
int main()
{
    int tot, outNum, nowNum = 1;
    Peo *now = n;            //指向目前报数的人的指针
    cin >> tot >> outNum;        //数据读入
    
    for (int i = 1; i < tot - 1; i++) 
    {
        n[i].front = n + i - 1;
        n[i].next = n + i + 1;
        n[i].ID = i + 1; 
    }
    n[0].front = n + tot - 1; 
    n[0].next = n + 1; 
    n[tot - 1].front = n + tot - 2;
    n[tot - 1].next = n;
    n[0].ID = 1; n[tot - 1].ID = tot;
    //初始化链表
    while (tot > 0) {
        if (nowNum == outNum) {
            cout << now->ID << " ";        //输出出局的人的编号
            _Cut(now);                    //出局
            nowNum = 1;                    //初始化数字
            tot--;                        //总人数-1
            now = now->next;            //下一个人
        }
        else {
            nowNum++;                    //数字+1
            now = now->next;            //下一个人
        }
    }
    return 0;
}