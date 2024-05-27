"""
3367 破损的楼梯
https://www.lanqiao.cn/problems/3367/learning

这是一个典型的线性DP问题，dp[i]表示到达第i阶楼梯的方法数
状态转移方程：dp[i]=dp[i-1]+dp[i-2]
状态压缩：dp[i]只与dp[i-1]和dp[i-2]有关，所以可以压缩
时间复杂度：O(n)
空间复杂度：O(n)
"""
N = int(1e5 + 10)
mod = int(1e9 + 7)
n, m = map(int, input().split())
a = list(map(int, input().split()))
vis = [0] * N
for i in a: vis[i] = 1
dp = [0] * N
dp[0] = 1
dp[1] = 1 - vis[1]
for i in range(2, n + 1):
    if vis[i]:
        continue
    dp[i] = (dp[i - 1] + dp[i - 2]) % mod
print(dp[n])
