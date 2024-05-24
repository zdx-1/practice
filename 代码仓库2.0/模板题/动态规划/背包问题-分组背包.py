"""
1178 小明的背包5
https://www.lanqiao.cn/problems/1178/learning
"""
# dp[i][j]表示第i组物品 体积为j的最大价值
n,v=map(int,input().split())
dp=[[0]*(v+1) for i in range(n+1)]
#n,v 表示多少组物品 以及小明的背包容量
for i in range(1,n+1):
  #对于每组物品 输入该组物品个数
  s=int(input())
  #对于每个物品 输入该物品的体积和价值
  for _ in range(s):
    wi,vi=map(int,input().split())
    for j in range(v+1):
      if j>=wi:
        dp[i][j]=max(dp[i][j],dp[i-1][j],dp[i-1][j-wi]+vi)
      else:
        dp[i][j]=max(dp[i][j],dp[i-1][j])
print(dp[n][v])