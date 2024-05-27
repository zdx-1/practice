"""
1177 小明的背包4
https://www.lanqiao.cn/problems/1177/learning
"""

N, V = map(int, input().split())
dp = [0]*(V+1)
for _ in range(N):
  w, v ,n= map(int, input().split())
  #如果n为0或者n*w大于等于V，说明该物品只能选择一次或者不能选择，因此直接使用01背包的方式更新dp列表
  if n==0 or n*w>=V:
    for j in range(w,V+1):
      dp[j] = max(dp[j], dp[j-w]+v)
  #否则，对于每个物品，使用完全背包的方式更新dp列表。
  elif n>0:
    for k in range(n):
      for j in range(V,w-1,-1):
        dp[j] = max(dp[j], dp[j-w]+v)
print(dp[-1])