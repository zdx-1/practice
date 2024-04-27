#include<bits/stdc++.h>
using namespace std;
const int MAXN = 1001;
int f[MAXN],n;
int main(){
    cin>>n;
    f[0] = 1, f[1] = 1;
    //从2到n按规律递推
    for(int i = 2;i <= n;i++)
        for(int j = 0;j < i;j++)
            f[i] += f[j] * f[i-j-1];//卡特兰数递推式
    cout<<f[n];
    return 0;
}   

