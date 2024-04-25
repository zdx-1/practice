#include<bits/stdc++.h>
using namespace std;
const int MAXN = 100000;
// 创建边结构
struct Edge{
	int v, w, next;
	// 下一个点，边权，当前边的上一个边
}edge[MAXN*MAXN];
int tot, head[MAXN];


// 建边
void AddEdge(int u, int v, int w) {
    // 建边
	edge[tot].v = v;
	edge[tot].w = w;
    // 连边
	edge[tot].next = head[u];
	head[u] = tot++;
}

int main() {
	// 初始化head
	memset(head, -1, sizeof(head));

	// 建边
	int t; cin >> t;
	for (int i = 0; i < t; i++) {
		int u, v, w;
		cin >> u >> v >> w;
		AddEdge(u, v, w);
	}
	// 遍历 u 连接的所有边
	int u; cin >> u;
	for (int i = head[u]; i != -1; i = edge[i].next) {
		cout << edge[i].v << " " << edge[i].w << endl;
	}
}

