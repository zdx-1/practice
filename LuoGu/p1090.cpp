#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;
 
int n, a1[99999], a2[99999];       //a1用于存剩余元素，a2用于存合并之后的元素
int ans, x;            //x为a2的元素个数
int main()
{
	cin >> n;
	memset(a1, 127, sizeof(a1));
	memset(a2, 127, sizeof(a2));
	for (int i = 0; i < n; i++)
		cin >> a1[i];
	sort(a1, a1 + n);
	int i = 0, j = 0, w;        //w为每次一消耗的体力
	for (int k = 1; k < n; k++)
	{
		w = a1[i] < a2[j] ? a1[i++] : a2[j++];			
		w += a1[i] < a2[j] ? a1[i++] : a2[j++];	
		a2[x++] = w;
		ans += w;
	}
	cout << ans;
 
	return 0;
}