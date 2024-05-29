import os
import sys

# 请在此输入您的代码
n = int(input())
s = [input() for _ in range(n)]
dp1 = [2] * n # dp1[i] 第i个字符串不翻转的最小长度
dp2 = [2] * n # dp2[i] 第i个字符串翻转的最小长度

for i in range(1, n): # 枚举每一个字符串
    # 1.dp1[i]从dp1[i-1]或dp2[i-1]转移
    k1 = dp1[i-1] + 2 - (s[i-1][1] == s[i][0])
    k2 = dp2[i-1] + 2 - (s[i-1][0] == s[i][0])
    dp1[i] = min(k1, k2)
    # 2.dp1[i]从dp1[i-1]或dp2[i-1]转移
    k3 = dp1[i-1] + 2 - (s[i-1][1] == s[i][1])
    k4 = dp2[i-1] + 2 - (s[i-1][0] == s[i][1])
    dp2[i] = min(k3, k4)

print(min(dp1[n-1], dp2[n-1]))
