#include<bits/stdc++.h>
using namespace std;
#include <vector>
#include <cstring>
typedef long long int LL;
const int mod = 1007;
const int base = 117;

vector<string> linker[mod + 2];
string s;
int ans;
void insert1(string s)
{
	int hash = 0;
	for (int i = 0; i < s.size(); i++)
	{
		hash = (hash*1ll*base + (LL)s[i]) % mod;
	}
 
	for (int i = 0; i < linker[hash].size(); i++)
		if (linker[hash][i] == s)return;
	linker[hash].push_back(s);
	ans++;
}
int main()
{
	int n;
	cin >> n;
	while (n--)
	{
		cin >> s;
		insert1(s);
	}
	cout << ans;
}
 