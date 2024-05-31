""" 基础DP """
""" 线性DP """

"""
破损的楼梯 https://www.lanqiao.cn/problems/3367/learning/
"""
import sys

input = sys.stdin.readline
mod = int(1e9 + 7)
n, m = map(int, input())
a = list(map(int, input().split()))
dp = [0] * (n + 1)
tp = [0] * (n + 1)
for i in a:
    tp[i] = 1

""" 二维DP """
"""
数字三角形 https://www.lanqiao.cn/problems/1536/learning
"""
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
dp = [[0] * (n + 1) for i in range(n)]
# 从下往上更新
for i in range(n - 1, -1, -1):
    for j in range(i + 1):
        if i == n - 1:
            dp[i][j] = a[i][j]
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1] + a[i][j])
print(dp[0][0])

n = int(input())
a = []
for i in range(n):
    a.append((list(map(int, input().split()))))
dp = [[0] * (n + 1) for i in range(n)]
# 从上往下更新
for i in range(n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + a[i][j]
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + a[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + a[i][j])
print(max(dp[n - 1]))

"""
摆花 https://www.lanqiao.cn/problems/389/learning
"""
MOD = 10 ** 6 + 7
n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
dp = [[0] * (m + 1) for i in range(n + 1)]
for i in range(n+1):
    dp[i][0] = 1
# 状态转移,当下做出的选择，利用之前dp,求dp[i][j]
for i in range(1,n+1):
    for j in range(1,m+1):
        for k in range(min(a[i],j)+1):
            dp[i][j]+=dp[i-1][j-k]
            dp[i][j]%=MOD
print(dp[n][m])


