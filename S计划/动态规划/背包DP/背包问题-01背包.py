"""
1174 小明的背包1
https://www.lanqiao.cn/problems/1174/learning
"""

# dp[i][j]    前i件物品，总体积不超过j 的最大价值
n, v = map(int, input().split())
dp = [[0] * (v + 1) for i in range(n + 1)]
a = []
b = [0]
for i in range(1, n + 1):
    wi, vi = map(int, input().split())
    for j in range(0, v + 1):
        if j >= wi:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wi] + vi)
            a.append("dp[{0}][{1}]=max(dp[{2}][{3}],dp[{4}][{5}]+{6}={7}".format(i, j, i - 1, j, i - 1, j - wi, vi,dp[i][j]))
            b.append("{}+{}".format(dp[i - 1][j - wi], vi))
        else:
            dp[i][j] = dp[i - 1][j]
            a.append("dp[{0}][{1}]=dp[{2}][{3}]={4}".format(i, j, i - 1, j, dp[i][j]))
            b.append(dp[i][j])
print(dp[n][v])
for i in a:
    print(i)
for i in range(1,len(b)):
    print("{:^6}".format(b[i]),end="\t")
    if i % 21 == 0:
        print()
