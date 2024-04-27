#include<iostream>
#include<queue>
using namespace std;
    
int main()
{
    int tot, outNum, nowNum = 1;
    queue<int> q;
    cin >> tot >> outNum;                        //读取数据
    for (int i = 1; i <= tot; i++)q.push(i);    //初始化队列
    while (!q.empty())                    //在队列不为空时继续模拟
    {
        if (nowNum == outNum)
        {
            cout << q.front() << " ";    //打印出局的人的编号
            q.pop();                    //出局
            nowNum = 1;                    //初始化现在的数字
        }
        else
        {
            nowNum++;
            q.push(q.front());            //排至队尾
            q.pop();
        }
    }
    cout << endl;
    return 0;
}