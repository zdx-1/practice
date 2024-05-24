"""
1174 小明的背包1
https://www.lanqiao.cn/problems/1174/learning
"""

#dp[i][j]    前i件物品，总体积不超过j 的最大价值
n,v=map(int,input().split())
dp=[[0]*(v+1) for i in range(n+1)]
for i in range(1,n+1):
  wi,vi=map(int,input().split())
  for j in range(0,v+1):
    if j>=wi:
      dp[i][j]=max(dp[i-1][j],dp[i-1][j-wi]+vi)
    else:
      dp[i][j]=dp[i-1][j]
print(dp[n][v])