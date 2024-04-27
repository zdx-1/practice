#include <bits/stdc++.h>
using namespace std;
#define AUTHOR 'HEX9CF'

//定义常量，边界值
const int maxn=100005;
int cnt=0;
int maxi[maxn];

struct Sedge
{
	int to;
	int next;
}edge[maxn];
int head[maxn];
void add(int u,int v)
{
	edge[cnt].to=v;
	edge[cnt].next=head[u];
	head[u]=cnt++;
}

void dfs(int x,int ori){
	if(maxi[x])// 如果已经标记过了，直接返回
		return;
	maxi[x]=ori;// 标记
	for(int i=head[x];i!=-1;i=edge[i].next)
		dfs(edge[i].to,ori); 
}
void read(int &x){
	char ch;
	x=0;
	while (!('0'<=ch&&ch<='9')) // 跳过非数字字符
	{
		ch=getchar(); // 读入
	}
	while ('0'<=ch&&ch<='9') // 读入数字
	{
		x=x*10+ch-'0';
		ch=getchar();
	}
}

int main(){
	int n,m;
	int a,b;
	memset(head,-1,sizeof(head));
	memset(maxi,0,sizeof(maxi));
	read(n);read(m);
	for(int i=1;i<=m;i++){
		read(a);read(b);
		add(b,a); // 添加边
	}
	for(int i=n;i;i--){
		dfs(i,i); 
	}
	for(int i=1;i<=n;i++){
		cout << maxi[i];
		if(i!=n)
			cout << " ";
	}
	return 0;
}






