"""
1176 小明的背包3
https://www.lanqiao.cn/problems/1176/learning
"""
#dp[i][j] =max(dp[i][j],dp[i-1][j-k*wi]+k*vi)  k属于(0，si)

n,v=map(int,input().split())
dp=[[0]*(v+1) for i in range(n+1)]
for i in range(1,n+1):
    wi,vi,si=map(int,input().split())
    for j in range(0,v+1):
        for k in range(0,min(si,j//wi)+1):
            dp[i][j]=max(dp[i][j],dp[i-1][j-k*wi]+k*vi)

print(dp[n][v])