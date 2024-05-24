"""
2049 蓝桥勇士
https://www.lanqiao.cn/problems/2049/learning
LIS 最长递增子序列：
1. 状态定义：dp[i]表示以a[i]结尾的最长递增子序列的长度
2. 状态转移方程：dp[i]=max(dp[j]+1) j<i and a[j]<a[i]
3. 边界条件：dp[0]=0
"""
n=int(input())
a=[0]+list(map(int,input().split()))
dp=[0]+[1]*n
for i in range(1,n+1):
    for j in range(1,i):
        if a[i]>a[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))