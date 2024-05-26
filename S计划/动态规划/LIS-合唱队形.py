"""
742 LIS-合唱队形
https://www.lanqiao.cn/problems/742/learning
思路：
1.求最长递增子序列的dp1
2.求最长递减子序列的dp2
3.求最长递增子序列和最长递减子序列的dp3
4.求dp3的最长子序列长度，然后取N-dp3的最长子序列长度的最小值
"""
import os
import sys

# 三种情况：（1）数组是纯增的（2）数组是纯减的（3）数组既有增又有减
# 对于第三种情况：将最长递增子序列和最短递增子序列的dp加在一起减1即可得到先增后减的dp
N = int(input())
mylist = list(map(int, input().split()))
dp1 = [1] * N
dp2 = [1] * N
dp3 = [0] * N
for i in range(N):
    for j in range(i):
        if mylist[i] > mylist[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

mylist.reverse()
for i in range(N):  # 数组反转求最长递增子序列的dp2
    for j in range(i):
        if mylist[i] > mylist[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

for i in range(N):
    dp3[i] = dp1[i] + dp2[N - 1 - i] - 1  # 自身重复需要减去1
print(min(N - max(dp1), N - max(dp2), N - max(dp3)))

"""
n = int(input())
a = [0] + list(map(int,input().split()))
dp1 = [0] * (n + 1)
for i in range(1, n + 1):
    dp1[i] = 1
    for j in range(1,i):
        if a[j] < a[i]:
            dp1[i] = max(dp1[i],dp1[j] + 1)

dp2 = [0] * (n + 1)
for i in range(n,0,-1):
    dp2[i] = 1
    for j in range(i + 1,n + 1):
        if a[j] < a[i]:
            dp2[i] = max(dp2[i],dp2[j] + 1)
ans = max(dp1[i] + dp2[i] - 1 for i in range(1,n + 1))
print(n - ans)
"""
