"""
1536 数字三角形
https://www.lanqiao.cn/problems/1536/learning
思路：
    1. 暴力递归
    2. 记忆化递归
    3. 动态规划
暴力递归超时
记忆化递归通过剪枝，可以解决
动态规划，通过状态转移方程，可以解决
"""
n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
dp=[[0]*n for i in range(n)]
for i in range(n):
    for j in range(i+1):
        if j==0: 
            dp[i][j]=dp[i-1][j]+a[i][j]
        elif j==i:
            dp[i][j]=dp[i-1][j-1]+a[i][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])+a[i][j]
print(max(dp[n-1]))
