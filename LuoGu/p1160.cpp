#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<list>
#include<cstring>
#include<string>
using namespace std;
const int N = 100005;
struct node {
	int l = 0, r = 0;
}L[N];
int h[N];
int main() {
	int n, m, head = 1;//初始化头节点为第一个同学
	cin >> n;
	memset(h, 1, sizeof(h));//h数组用来检查第i个同学有没有被删除，置1。
	int k, p;
	for (int i = 2; i <= n; ++i) {
		scanf("%d %d", &k, &p);
		if (p == 0) {
			if (L[k].l) {//如果k同学左边还有同学
				L[L[k].l].r = i;//先修改k左边的同学的右边为i
				L[i].l = L[k].l;
			}
			L[i].r = k;//注意不能写在if (L[k].l)前。
			L[k].l = i;
			if (head == k) {//k为头节点的话，i又插入在k左边，则将head=i；
				head = i;
			}
		}
		else {
			//同上
			if (L[k].r) {
				L[L[k].r].l = i;
				L[i].r = L[k].r;
			}
			L[i].l = k;
			L[k].r = i;
		}
	}
	cin >> m;
	int cur;
	while (m--) {
		scanf("%d", &cur);
		if (h[cur]) {//cur没有被删除
			int tmp = L[cur].l;
			if (L[cur].l) {
				L[L[cur].l].r = L[cur].r;
			}else {//如果左边没有节点，则需要修改头节点
				head = L[cur].r;
			}
			if (L[cur].r) {
				L[L[cur].r].l = tmp;
			}
			h[cur] = 0;
		}
 
	}
	for (int i = head; i != 0; i = L[i].r) {
		printf("%d ", i);
	}
	return 0;
}