```c++
#include <bits/stdc++.h>
using namespace std;

const int M = 1005;

struct PII
{
    int first;
    int second;
};

// C++ 有个数据类型叫 pair 上面的就可以定义为 pair<int,int> 用起来比较方便。


PII tempPair;//临时结点

char Map[M][M];


//---------图的路径搜索常用方向移动表示-------

int dx[4]= {0,1,-1,0};

int dy[4]= {1,0,0,-1};

// 两两组合形成上下左右四个方向
//      1------------------> x
//      |
//      |
//      |
//      |
//      |
//      |
//      |
//      ↓
//      y

// dx[0]=0 dy[0]=1 那么代表向下的方向

// dx[1]=1 dy[1]=0 那么代表向右的方向

// dx[2]=-1 dy[0]=0 那么代表向左的方向

// dx[3]=0 dy[1]=-1 那么代表向上的方向

int n;// n 行
int m;// m 列
int k;// k 次

queue<PII > q; //广度优先搜索所用的队列

int len;//记录节点数量方便后续k的计算

bool pd(int x, int y)
{

    if(x<1)
        return 0;
    // /x 轴坐标 左侧越界

    else if(x>n)
        return 0;
    //x 轴坐标 右侧越界

    else  if(y<1)
        return 0;
    //y 轴坐标 上侧越界

    else if(y>m)
        return 0;
    //y 轴坐标 下侧越界

    else if(Map[x][y]=='g')
        return 0;
    //已经长草了

    else return 1;
    // 在范围内，且没长草
}

void BFS()
{
    //BFS
    while(!q.empty()&&k>0)
    {
        tempPair = q.front();

        q.pop();
        //这两步是取出队首的节点


        int x = tempPair.first;//横坐标
        int y = tempPair.second;//纵坐标



        for(int i=0; i<4; i++)
        {
            int nowx = x+dx[i]; //扩展后的横坐标
            int nowy = y+dy[i]; //扩展后的纵坐标



            if(pd(nowx,nowy))
            {

                q.push({nowx,nowy});
                Map[nowx][nowy]='g';
            }
            //符合要求执行扩展，不符合要求，忽略即可。

        }

        len--; //没取出一个节点len  -1

        if(len==0)
        {
            //当len =0 时，代表当前层扩展完了，那么就代表第一个月扩展完了

            k--; // 所以k--

            len = q.size(); // 当前层扩展完了，那就该扩展下一层了，所以len又被赋值为下一层的节点数目的值
        }
    }

}
int main()
{
    cin>>n>>m;



    for(int i=1; i<=n; i++)
    {
        for(int j=1; j<=m; j++)
        {
            cin>>Map[i][j];


            if(Map[i][j]=='g')
            {
                tempPair.first=i;
                tempPair.second=j;
               // cout<<i<<""<<j<<endl;
                q.push(tempPair);//将初始有树的结点加入队列
            }
        }
    }

    len = q.size();//记录第一层的节点数量方便后续k的计算

    cin>>k;

    BFS();

    for(int i=1; i<=n; i++)
    {

        for(int j=1; j<=m; j++)
        {
            cout<<Map[i][j];
        }

        cout<<endl;
    }

    return 0;
}

```

```python
# 请在此输入您的代码
from queue import Queue

dx = [0, 1, -1, 0]

dy = [1, 0, 0, -1]

# 两两组合形成上下左右四个方向
#      1------------------> x
#      |
#      |
#      |
#      |
#      |
#      |
#      |
#      ↓
#      y

# dx[0]=0 dy[0]=1 那么代表向下的方向

# dx[1]=1 dy[1]=0 那么代表向右的方向

# dx[2]=-1 dy[0]=0 那么代表向左的方向

# dx[3]=0 dy[1]=-1 那么代表向上的方向

Map = []

q = Queue()

n = 0
m = 0
k = 0

length = 0


def pd(x, y):
    global n, m, Map

    if x < 0:
        return False

    # x 轴坐标左侧越界

    elif x >= n:
        return False
    # x 轴坐标右侧越界

    elif y < 0:
        return False
    # y轴坐标上侧越界

    elif y >= m:
        return False
    # y 轴坐标下侧越界

    elif Map[x][y] == 'g':
        return False
    # 已经长草了

    else:
        return True

    # 在范围内，且没长草


def BFS():

    global k, q, n, m, Map, length

    while k > 0 & (not q.empty()):

        tempPair = q.get()

        x = tempPair[0]  # 横坐标

        y = tempPair[1]  # 纵坐标

        nowx=x+1

        if (pd(nowx, y)):
            q.put((nowx, y))
            Map[nowx][y] = 'g'

        nowx=x-1

        if (pd(nowx, y)):
            q.put((nowx, y))
            Map[nowx][y] = 'g'

        nowy=y+1
        if (pd(x, nowy)):
            q.put((nowx, nowy))
            Map[x][nowy] = 'g'

        nowy=y-1
        if (pd(x, nowy)):
            q.put((nowx, nowy))
            Map[x][nowy] = 'g'

        length -= 1

        if length == 0:
            k -= 1
            length = q.qsize()


if __name__ == '__main__':

    n, m = map(int, input().split())

    Map = [[0 for _ in range(m)] for _ in range(n)]  # Python 动态开数组会减少运行时间

    for i in range(n):
        input_ = input()
        for j in range(m):
            Map[i][j] = input_[j]
            if Map[i][j] == 'g':
                q.put((i, j))

    k = int(input())

    length = q.qsize()

    BFS()
    for i in range(n):
        str_temp = ''
        for j in range(m):
            str_temp += Map[i][j]
        print(str_temp)


```

Python 的 Queue 非常耗费时间，强烈建议大家使用 list 进行模拟

下面是用 List 模拟，使用 Queue 耗时 3000 ms , 使用 list 模拟仅消耗 54 ms 所以大家使用 Python 编写代码的时候还是使用 List 尽量避免 Queue 的使用。(使用Deque也可以)



```python
# 请在此输入您的代码
from queue import Queue

dx = [0, 1, -1, 0]

dy = [1, 0, 0, -1]

# 两两组合形成上下左右四个方向
#      1------------------> x
#      |
#      |
#      |
#      |
#      |
#      |
#      |
#      ↓
#      y

# dx[0]=0 dy[0]=1 那么代表向下的方向

# dx[1]=1 dy[1]=0 那么代表向右的方向

# dx[2]=-1 dy[0]=0 那么代表向左的方向

# dx[3]=0 dy[1]=-1 那么代表向上的方向

Map = []

q = []
qfront = 0
qend = 0

n = 0
m = 0
k = 0

length = 0


def pd(x, y):
    if x < 0:
        return False

    # x 轴坐标左侧越界

    elif x >= n:
        return False
    # x 轴坐标右侧越界

    elif y < 0:
        return False
    # y轴坐标上侧越界

    elif y >= m:
        return False
    # y 轴坐标下侧越界

    elif Map[x][y] == 'g':
        return False
    # 已经长草了

    else:
        return True

    # 在范围内，且没长草


def BFS():
    global k, q, n, m, Map, length, qend, qfront
    # print("K Length", k, length)
    while k > 0 and length > 0:

        tempPair = q[qfront]


        qfront += 1
        x = tempPair[0]  # 横坐标

        y = tempPair[1]  # 纵坐标

        for i in range(4):

            nowx = x + dx[i]  # 扩展后的横坐标

            nowy = y + dy[i]  # 扩展后的纵坐标

            if (pd(nowx, nowy)):
                q.append((nowx,nowy))
                qend += 1
                Map[nowx][nowy] = 'g'
        length -= 1

        if length == 0:
            k -= 1
            length = qend - qfront


if __name__ == '__main__':

    n, m = map(int, input().split())

    Map = [[0 for _ in range(m)] for _ in range(n)]  # Python 动态开数组会减少运行时间

    for i in range(n):
        input_ = input()
        for j in range(m):
            Map[i][j] = input_[j]
            if Map[i][j] == 'g':
                q.append((i,j))
                qend += 1

    k = int(input())

    length = qend - qfront

    BFS()
    for i in range(n):
        str_temp = ''
        for j in range(m):
            str_temp += Map[i][j]
        print(str_temp)
        
```

```java 
import java.util.*;
import java.util.concurrent.LinkedBlockingQueue;

import static java.lang.Math.abs;

public class Main {

    static final int M = 1005;

    static class PII
    {
        public int first;
        public int second;
    };



    static String Map[]=new String[M];


//---------图的路径搜索常用方向移动表示-------

    static int dx[]= {0,1,-1,0};

    static  int dy[]= {1,0,0,-1};

// 两两组合形成上下左右四个方向
//      1------------------> x
//      |
//      |
//      |
//      |
//      |
//      |
//      |
//      ↓
//      y

// dx[0]=0 dy[0]=1 那么代表向下的方向

// dx[1]=1 dy[1]=0 那么代表向右的方向

// dx[2]=-1 dy[0]=0 那么代表向左的方向

// dx[3]=0 dy[1]=-1 那么代表向上的方向

    static int n;// n 行
    static int m;// m 列
    static int k;// k 次

    static Queue<PII > q= new LinkedBlockingQueue<>();
    //广度优先搜索所用的队列

    static int len;//记录节点数量方便后续k的计算

    static boolean pd(int x, int y)
    {

        if(x<1)
            return false;
            // /x 轴坐标 左侧越界

        else if(x>n)
            return false;
            //x 轴坐标 右侧越界

        else  if(y<1)
            return false;
            //y 轴坐标 上侧越界

        else if(y>m)
            return false;
            //y 轴坐标 下侧越界

        else if(Map[x].charAt(y)=='g')
            return false;
            //已经长草了

        else return true;
        // 在范围内，且没长草
    }

    static void BFS()
    {
        //BFS
        while(q.size()!=0&&k>0)
        {

            PII tempPair= q.peek();
            q.poll();
            //这两步是取出队首的节点
//            System.out.println(q.size());


            int x = tempPair.first;//横坐标
            int y = tempPair.second;//纵坐标



            for(int i=0; i<4; i++)
            {
                int nowx = x+dx[i]; //扩展后的横坐标
                int nowy = y+dy[i]; //扩展后的纵坐标



                if(pd(nowx,nowy))
                {
                    PII tempPair2=new PII();//临时结点
                    tempPair2.first=nowx;
                    tempPair2.second=nowy;

                    q.add(tempPair2);

                    StringBuilder strBuilder = new StringBuilder(Map[nowx]);
                    strBuilder.setCharAt(nowy, 'g');
                    Map[nowx]=strBuilder.toString();


                }
                //符合要求执行扩展，不符合要求，忽略即可。

            }

            len--; //没取出一个节点len  -1

            if(len==0)
            {
                //当len =0 时，代表当前层扩展完了，那么就代表第一个月扩展完了

                k--; // 所以k--

                len = q.size(); // 当前层扩展完了，那就该扩展下一层了，所以len又被赋值为下一层的节点数目的值
            }
        }

    }

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);


        n = in.nextInt();
        m = in.nextInt();
        for(int i=1; i<=n; i++)
        {
            Map[i]=new String(" " +in.next());
            for(int j=1; j<=m; j++)
            {
                char temChar = Map[i].charAt(j);


                if(temChar=='g')
                {
                    PII tempPair=new PII();//临时结点
                    tempPair.first=i;
                    tempPair.second=j;


                    q.offer(tempPair);//将初始有草的结点加入队列
                }
            }
        }

        len = q.size();//记录第一层的节点数量方便后续k的计算

        k= in.nextInt();


        BFS();

        for(int i=1; i<=n; i++)
        {

            System.out.println(Map[i]);
        }

    }
}
```

