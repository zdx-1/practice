```c++
#include <bits/stdc++.h>
using namespace std;

int vis[150][150]; //用于存储是否访问过，并且存储长度

char G[150][150]; //用于存储题目给出的地图

int n,m,ans=0;

int dx[4] = {0,0,-1,1};

int dy[4] = {1,-1,0,0};

//上下左右移动，不会的看前面的代码

struct node
{
    int x;
    int y;
};

node Start,End;
bool pd(int x,int y)
{


    if(x<1)
        return 0;
    //从左侧走出方格

    else if(x>n)
        return 0;
    //从右侧走出方格

    else if(y<1)
        return 0;
    //从上侧走出方格

    else if(y>m)
        return 0;
    //从下侧走出方格

    else if( vis[x][y]!=0)
        //已经访问了
        return 0;
    else if(G[x][y]!='1') return 0;
    //不是路不能走
    else return 1;
}

bool  check(int x, int y)
{

    if(x == End.x&& y == End.y)   //找到终点，把距离给他
    {
        ans  =  vis[x][ y];
        return 1;
    }

    else    return 0;

}
void bfs()
{
    queue<node>q;

    node now,next;

    q.push(Start);     //将起点压人队列中

    vis[Start.x][Start.y] = 1;

    while(!q.empty())
    {
        now = q.front();

        if(check(now.x,now.y))
            return ;

        q.pop();     //将队列最前面的弹出。

        for(int i=0; i<4; i++)  //四个方向
        {

            int nextx = now.x + dx[i];
            int nexty = now.y + dy[i];

            if(pd(nextx,nexty))  //判断是否符合条件
            {

                next.x=nextx;
                next.y=nexty;

                q.push(next);

                vis[nextx][nexty] = vis[now.x][now.y]+1; //步数+1
            }
        }
    }
}
int main()
{
    cin>>n>>m;
    //memset(vis,0,sizeof(vis));
    for(int i=1; i<=n; i++)
    {
        for(int j=1; j<=m; j++)
        {
            cin>>G[i][j];
        }
    }

    cin>>Start.x>>Start.y>>End.x>>End.y;

    ans = 0;

    bfs();
    cout<<ans-1<<endl;

    return 0;
}


```

```python
dx = [0, 1, -1, 0]

dy = [1, 0, 0, -1]

G = []

Vis = []

# --------队列模拟-----------
q = []                   # |
                       # |
qfront = 0               # |
                       # |
qend = 0                 # |
# --------队列模拟-----------


n = 0
m = 0
ans = 0

startX=0
startY=0

endX=0
endY=0

def pd(x, y):
  if x < 1:
      return False

  # x 轴坐标左侧越界

  elif x > n:
      return False
  # x 轴坐标右侧越界

  elif y < 1:
      return False
  # y轴坐标上侧越界

  elif y > m:
      return False
  # y 轴坐标下侧越界

  elif Vis[x][y]!=0:
      return False
  #已经访问了
  elif G[x][y] != '1':
      return False
  # 已经访问了
  else:
      return True

  # 在范围内，且没长草

def check( x,  y):

  global ans
  if x == endX and y == endY :  #找到终点，把距离给他

      ans  =  Vis[x][y];

      return True;

  else   :
      return False;

def BFS():


  global qend ,qfront

  q.append((startX,startY))

  qend+=1

  Vis[startX][startY]=1

  while qend-qfront!=0:

      tempPair = q[qfront]
      qfront+=1

      x = tempPair[0]  # 横坐标

      y = tempPair[1]  # 纵坐标
      if check(x,y):
          return

      for i in range(4):

          nowx = x + dx[i]  # 扩展后的横坐标

          nowy = y + dy[i]  # 扩展后的纵坐标

          if (pd(nowx, nowy)):

              q.append((nowx,nowy))
              qend+=1

              Vis[nowx][nowy] = Vis[x][ y] + 1


if __name__ == '__main__':

  n, m = map(int, input().split())

  G = [[0 for _ in range(m+10)] for _ in range(n+10)]  # Python 动态开数组会减少运行时间

  Vis = [[0 for _ in range(m+10)] for _ in range(n+10)]  # Python 动态开数组会减少运行时间

  for i in range(n):
      input_ = input().split()
      for j in range(m):
          G[i+1][j+1] = input_[j]

  startX ,startY , endX ,endY = map(int, input().split())

  BFS()

  print(ans-1)

```

```java
import java.util.*;
import java.util.concurrent.LinkedBlockingQueue;

import static java.lang.Math.abs;

public class Main {

    static final int M = 1005;


    static class node {
        public int x;
        public int y;

        public node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    ;

    static int n, m, ans = 0;
    static int vis[][] = new int[150][150]; //用于存储是否访问过，并且存储长度

    static int G[][] = new int[150][150];  //用于存储题目给出的地图

    static node Start, End;
//---------图的路径搜索常用方向移动表示-------

    static int dx[] = {0, 1, -1, 0};

    static int dy[] = {1, 0, 0, -1};


    static Queue<node> q = new LinkedBlockingQueue<>();
    //广度优先搜索所用的队列


    static boolean pd(int x, int y) {

        if (x < 1)
            return false;
            // /x 轴坐标 左侧越界

        else if (x > n)
            return false;
            //x 轴坐标 右侧越界

        else if (y < 1)
            return false;
            //y 轴坐标 上侧越界

        else if (y > m)
            return false;
            //y 轴坐标 下侧越界

        else if (vis[x][y] != 0)
            //已经访问了
            return false;

        else if (G[x][y] != 1)
            //不能走
            return false;

        else return true;
        // 在范围内，且没长草
    }

    static boolean check(int x, int y) {

        if (x == End.x && y == End.y)   //找到终点，把距离给他
        {
            ans = vis[x][y];
            return true;
        } else return false;

    }

    static void BFS() {

        q.add(Start);

        vis[Start.x][Start.y] = 1;

        node now, next;

        while (q.size() != 0) {

            now = q.peek();

            if (check(now.x, now.y))
                return;

            q.poll();
            //这两步是取出队首的节点


            for (int i = 0; i < 4; i++)  //四个方向
            {

                int nextx = now.x + dx[i];
                int nexty = now.y + dy[i];

                if (pd(nextx, nexty))  //判断是否符合条件
                {

                    next = new node(nextx, nexty);

                    q.add(next);

                    vis[nextx][nexty] = vis[now.x][now.y] + 1; //步数+1
                }
            }


        }

    }

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);


        n = in.nextInt();
        m = in.nextInt();
        for (int i = 1; i <= n; i++) {

            for (int j = 1; j <= m; j++) {
                G[i][j] = in.nextInt();
            }
        }


        int startX = in.nextInt();
        int startY = in.nextInt();
        int endX = in.nextInt();
        int endY = in.nextInt();

        Start=new node(startX,startY);
        End=new node(endX,endY);
        BFS();

        System.out.println(ans-1);
    }
}


```

