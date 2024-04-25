#include <iostream>
#include <cstdio>
using namespace std;
class Edge{
public:
    int to,next;
};
class Graph{
public:
    Edge *edges;
    int *head;
    int n,m;
    Graph(int n,int m){
        this->n=n;
        this->m=m;
        edges=new Edge[m+1];
        head=new int[n+1];
        for(int i=0;i<=n;i++)
            head[i]=-1;
    }
    void addEdge(int u,int v){

        
        edges[m].to=v;
        edges[m].next=head[u];
        head[u]=m++;
    }
};
int main(){
    int n,m,u,v;
    scanf("%d%d",&n,&m);
    Graph g(n,m);
    for(int i=0;i<m;i++){
        scanf("%d%d",&u,&v);
        g.addEdge(u,v);
    }
    for(int i=1;i<=n;i++){
        printf("%d:",i);
        for(int j=g.head[i];j!=-1;j=g.edges[j].next)
            printf(" %d",g.edges[j].to);
        printf("\n");
    }
    system("pause");
    return 0;
}
