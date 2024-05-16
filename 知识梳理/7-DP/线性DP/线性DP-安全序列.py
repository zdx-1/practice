"""
3423 安全序列
https://www.lanqiao.cn/problems/3423/learning
线性DP：
状态定义：f[i]表示长度为i的安全序列的个数
状态转移方程：f[i] = f[i-1] + f[i-k-1]
边界条件：f[0] = 1
时间复杂度：O(n)
空间复杂度：O(n)
"""
n, k = map(int, input().split())
f = [0]*(n+10)
f[0] = 1
mod = int(1e9 + 7)
for i in range(1, n + 1, 1):
    f[i] = f[i - 1]
    if i >= k + 1:
        f[i] = (f[i] + f[i - (k + 1)])%mod
    else:
        f[i] = f[i] + 1
print(f[n])