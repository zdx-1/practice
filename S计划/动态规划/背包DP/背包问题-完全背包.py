"""
1175 小明的背包2
https://www.lanqiao.cn/problems/1175/learning
"""
# dp[i][j]=max(dp[i-1][j],dp[i][j-wi]+vi)
# 不取或在先前基础上取第i种（所以可以取多次）
n, v = map(int, input().split())
dp = [[0] * (v + 1) for i in range(n + 1)]
a = []
b = [0]
for i in range(1, n + 1):
    wi, vi = map(int, input().split())

    for j in range(0, v + 1):
        if j >= wi:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - wi] + vi)
            a.append(
                "dp[{0}][{1}]=max(dp[{2}][{3}],dp[{4}][{5}]+{6}={7}".format(i, j, i - 1, j, i, j - wi, vi, dp[i][j]))
            b.append("{},{}+{}".format(dp[i - 1][j], dp[i - 1][j - wi], vi))
        else:
            dp[i][j] = dp[i - 1][j]
            a.append("dp[{0}][{1}]=dp[{2}][{3}]={4}".format(i, j, i - 1, j, dp[i][j]))
            b.append(dp[i][j])
print(dp[n][v])
for i in a:
    print(i)
for i in range(21):
    print("{:^10}".format(i), end="||")
print()
for i in range(1, len(b)):
    print("{:^10}".format(b[i]), end="||")
    if i % 21 == 0:
        print()
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
# 有点延迟，但是可以接受，比起原来的那个键盘还是好用一些的
