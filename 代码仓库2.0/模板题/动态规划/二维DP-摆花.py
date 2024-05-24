"""
389 摆花
https://www.lanqiao.cn/problems/389/learning
二维DP问题：
1. 状态定义：dp[i][j]表示前i行，第j列的方案数
2. 状态转移方程：
    dp[i][j]=dp[i-1][j-k]+dp[i-1][j-k-1]+...+dp[i-1][j-1]
    其中k为a[i]和j的最小值
3. 初始状态：dp[0][0]=1
4. 输出：dp[n][m]%(1e6+7)
"""
n, m = map(int, input().split())
a=[0]+list(map(int, input().split()))
dp=[[0]*(m+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0]=1
for i in range(1,n+1):
    for j in range(1,m+1):
        for k in range(min(a[i],j)+1):
            dp[i][j]+=dp[i-1][j-k]
            dp[i][j]%=int(1e6+7)
print(dp[n][m])