# n = int(input())
# a = []
# for i in range(n):
#     a.append(list(map(int, input().split())))
#
# dp = [[0] * n for i in range(n)]
# for i in range(n):
#     for j in range(i + 1):
#         if j == 0:
#             dp[i][j] = dp[i - 1][j] + a[i][j]
#         elif j == i:
#             dp[i][j] = dp[i - 1][j - 1] + a[i][j]
#         else:
#             dp[i][j] = max(dp[i - 1][j], dp[i-1][j - 1] + a[i][j])
# print(max(dp[n - 1]))

# n = int(input())
# a = []
# for i in range(n):
#     a.append(list(map(int, input().split())))
# dp = [[0] * n for i in range(n)]
# for i in range(n):
#     for j in range(i + 1):
#         if j == 0:
#             dp[i][j] = dp[i - 1][j] + a[i][j]
#         elif j == i:
#             dp[i][j] = dp[i - 1][j - 1] + a[i][j]
#         else:
#             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + a[i][j]
# print(max(dp[-1]))

# """最长上升子序列"""
# n, m = map(int, input().split())
# s = list(map(int, input().split()))
# t = list(map(int, input().split()))
#
# f = [0] * (m + 1)
# ans = 0
# for i in range(n):
#     per = 0
#     for j in range(m):
#         if s[i] == t[j] and f[j + 1] < per + 1:
#             f[j + 1] = per + 1
#         if s[i] > t[j] and per < f[j + 1]:
#             per = f[j + 1]
#         if ans < f[j + 1]:
#             ans = f[j + 1]
# print(ans)

"""LIS"""
# N = int(input())
# mylist = list(map(int, input().split()))
# dp1 = [1] * N
# dp2 = [1] * N
# dp3 = [0] * N
# for i in range(N):
#     for j in range(i):
#         if mylist[i] > mylist[j]:
#             dp1[i] = max(dp1[i], dp1[j] + 1)
# mylist.reverse()
# for i in range(N):
#     for j in range(i):
#         if mylist[i] > mylist[j]:
#             dp2[i] = max(dp2[i], dp2[j] + 1)
# for i in range(N):
#     dp3[i] = dp1[i] + dp2[N - 1 - i] - 1
# print(min(N - max(dp1), N - max(dp2), N - max(dp3)))


# n = list(map(int, list(str(input()))))
# n.sort()
# cnt = n.count(0)
# maxn = ""
# minn = str(n[cnt])
# if cnt > 0:
#     minn += str("0" * cnt)
# for i in n[::-1]:
#     maxn += str(i)
# for i in n[cnt + 1::1]:
#     minn += str(i)
# print(maxn)
# print(minn)

