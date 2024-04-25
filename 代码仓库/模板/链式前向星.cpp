#include<iostream>
#include<cstdio>
using namespace std;
const int N=100005;
int n,m;
struct Edge
{
	int to,next;
}edge[N<<1];
int head[N],cnt;
void add_edge(int u,int v)
{
	edge[++cnt]=(Edge){v,head[u]};
	head[u]=cnt;
}

int main()
{

    while(scanf("%d%d",&n,&m)!=EOF)
    {
        for(int i=1;i<=n;i++)
            head[i]=0;
        cnt=0;
        for(int i=1;i<=m;i++)
        {
            int u,v;
            scanf("%d%d",&u,&v);
            add_edge(u,v);
            add_edge(v,u);
        }
        for(int i=1;i<=n;i++)
            printf("%d ",head[i]);
        printf("\n");
    }
    return 0;
}

