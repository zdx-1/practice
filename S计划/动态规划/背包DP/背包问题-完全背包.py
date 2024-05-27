"""
1175 小明的背包2
https://www.lanqiao.cn/problems/1175/learning
"""
# dp[i][j]=max(dp[i-1][j],dp[i][j-wi]+vi)  
# 不取或在先前基础上取第i种（所以可以取多次）
n,v=map(int,input().split())
dp=[[0]*(v+1) for i in range(n+1)]
for  i in range(1,n+1):
    wi,vi=map(int,input().split())
    for j in range(0,v+1):
        if (j>=wi):
            dp[i][j]=max(dp[i-1][j],dp[i][j-wi]+vi)
        else:
            dp[i][j]=dp[i-1][j]
print(dp[n][v])

#使用滚动数组进行优化
"""
N,V=map(int,input().split())
dp=[0]*(V+1)
for i in range(1,N+1):
  w,v=map(int,input().split())
  for j in range(w,V+1):
    dp[j]=max(dp[j],dp[j-w]+v)
print(dp[V])
"""