#include<bits/stdc++.h>
using namespace std;
const int MAXN = 100000;
// �����߽ṹ
struct Edge{
	int v, w, next;
	// ��һ���㣬��Ȩ����ǰ�ߵ���һ����
}edge[MAXN*MAXN];
int tot, head[MAXN];


// ����
void AddEdge(int u, int v, int w) {
    // ����
	edge[tot].v = v;
	edge[tot].w = w;
    // ����
	edge[tot].next = head[u];
	head[u] = tot++;
}

int main() {
	// ��ʼ��head
	memset(head, -1, sizeof(head));

	// ����
	int t; cin >> t;
	for (int i = 0; i < t; i++) {
		int u, v, w;
		cin >> u >> v >> w;
		AddEdge(u, v, w);
	}
	// ���� u ���ӵ����б�
	int u; cin >> u;
	for (int i = head[u]; i != -1; i = edge[i].next) {
		cout << edge[i].v << " " << edge[i].w << endl;
	}
}

