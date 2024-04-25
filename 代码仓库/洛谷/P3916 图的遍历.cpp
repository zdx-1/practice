#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;
#define MAXL 100010
int N,M,A[MAXL];
vector<int> G[MAXL];

void dfs(int x,int d){
	if(A[x]) return;
	A[x]=d;
	for (int i =0;i<G[x].size();i++)
		dfs(G[x][i],d)
}
