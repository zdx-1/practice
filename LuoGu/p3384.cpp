#include<bits/stdc++.h>
using namespace std;
struct Treenode{
	int left,right,father,val;
}node[101];
struct Station{
	int pos,step;
};
int width[101],visited[101];
int dfs(Treenode nod,int deep)
{
	if(nod.val!=0)
	width[deep]++;
	if(nod.left==0&&nod.right==0)
	return 1;
	else
	return max(dfs(node[nod.left],deep+1),dfs(node[nod.right],deep+1))+1;
}
int main()
{
	int n,i,u,v,x,y;
	cin>>n;
	for(i=0;i<=n;i++)
	{
		node[i].val=i;
	}
	for(i=1;i<n;i++)
	{
		cin>>u>>v;
		if(!node[u].left)
		node[u].left=v;
		else
		node[u].right=v;
		node[v].father=u;
	}
	cin>>x>>y;
	int ans,wide=0;
	ans=dfs(node[1],1);
	for(i=1;i<=n;i++) 
	wide=max(wide,width[i]);
	cout<<ans<<endl<<wide<<endl;
	
	
	Station tn={x,0};
	queue<Station> tem;
	memset(visited,0,sizeof(visited));
	visited[x]=1;
	tem.push(tn);
	while(!tem.empty())
	{
		Station nodes=tem.front();
		tem.pop();
		if(nodes.pos==y)
		{
			cout<<nodes.step;
			break;
		}
		int left=node[nodes.pos].left,right=node[nodes.pos].right,father=node[nodes.pos].father,step=nodes.step;
		if(left&&!visited[left])
		{
			visited[left]=1;
			tem.push({left,step+1});
		}
		if(right&&!visited[right])
		{
			visited[right]=1;
			tem.push({right,step+1});
		}
		if(father&&!visited[father])
		{
			visited[father]=1;
			tem.push({father,step+2});
		}
	}
	return 0;
}