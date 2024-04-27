#include <iostream>
#include <cstring>
using namespace std;
#define AUTHOR "HEX9CF"

const int maxn = 100005;

int cnt = 0;
int maxi[maxn];

// 链式前向星
struct Sedge
{
    int to;
    int next;
} edge[maxn];
int head[maxn];

void add(int u, int v)
{
    edge[cnt].to = v;
    edge[cnt].next = head[u];
    head[u] = cnt++;
}

void dfs(int x, int ori)
{
    if (maxi[x])
    {
        return;
    }
    maxi[x] = ori;
    for (int i = head[x]; ~i; i = edge[i].next)
    {
        dfs(edge[i].to, ori);
    }
}

void read(int &x)
{
    char ch;
    x = 0;
    while (!('0' <= ch && '9' >= ch))
    {
        ch = getchar();
    }
    while (('0' <= ch && '9' >= ch))
    {
        x = x * 10 + ch - '0';
        ch = getchar();
    }
}

int main()
{
    int n, m;
    int a, b;
    memset(head, -1, sizeof(head));
    memset(maxi, 0, sizeof(maxi));
    read(n);
    read(m);
    for (int i = 1; i <= m; i++)
    {
        read(a);
        read(b);
        add(b, a); // 反向添加边
    }
    for (int i = n; i; i--)
    {
        // 反向搜索
        dfs(i, i);
    }
    for (int i = 1; i <= n; i++)
    {
        cout << maxi[i];
        if (i != n)
        {
            cout << " ";
        }
    }
    return 0;
}
