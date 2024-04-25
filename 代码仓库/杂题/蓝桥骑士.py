# import sys
# from bisect import bisect_right

# n = int(sys.stdin.readline())
# r = list(map(int, sys.stdin.readline().split()))
# dp = [0]
# for i in range(n):
#     if r[i] > dp[-1]:
#         dp.append(r[i])
#     elif r[i] < dp[-1]:
#         dp[bisect_right(dp, r[i])] = r[i]
# print(len(dp) - 1)

n=int(input())
a=list(map(int,input().split()))
b=[a[0]]
for i in range(1,n):
    if a[i] > b[-1]:
        b.append(a[i])
print(len(b))


import bisect
n = int(input())
a = list(map(int, input().split()))
b = [a[0]]
for i in range(1, n):
    # 找b中第一个 >= a[i]的元素
    idx = bisect.bisect_left(b, a[i])
    # 没有 >= a[i]的元素
    if idx == len(b):
        b.append(a[i])
    else:
        b[idx] = a[i]
print(len(b))