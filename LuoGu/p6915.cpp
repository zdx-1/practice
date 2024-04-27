#include<bits/stdc++.h>
#define Tp template<typename Ty>
#define Ts template<typename Ty,typename... Ar>
#define Rg register
#define RI Rg int
#define Cn const
#define CI Cn int&
#define I inline
#define W while
#define N 20
#define fi first
#define se second
#define LL long long
#define DB long double
using namespace std;
int n,C[N+5][N+5];DB p[4];typedef pair<DB,LL> Pr;priority_queue<Pr,vector<Pr>,greater<Pr> > q;
I void dfs(CI x,CI t,DB w,Cn LL& s)//暴搜可能状态
{
	if(x==3) {for(RI i=1;i<=t;++i) w*=p[x];q.push(make_pair(w,s));return;}//概率和个数绑成pair扔入堆
	for(RI i=0;i<=t;++i) dfs(x+1,t-i,w,s*C[t][i]),w*=p[x];
}
int main()
{
	RI i,j;for(scanf("%d",&n),i=0;i^4;++i) scanf("%Lf",p+i);
	for(C[0][0]=i=1;i<=n;++i) for(C[i][0]=j=1;j<=i;++j) C[i][j]=C[i-1][j-1]+C[i-1][j];
	#define Push(x,y) (q.push(make_pair(x,y)),ans+=(x)*(y))//合并得到y个x，扔入堆，同时统计答案
	dfs(0,n,1,1);Pr k,o;DB ans=0;W(!q.empty()) k=q.top(),q.pop(),
		k.se>1&&Push(2*k.fi,k.se>>1),k.se&1&&!q.empty()&&(o=q.top(),q.pop(),--o.se&&(q.push(o),0),Push(k.fi+o.fi,1));//尽可能自己两两配对，若有剩余和新的堆顶配对
	return printf("%.4Lf\n",ans),0;
}