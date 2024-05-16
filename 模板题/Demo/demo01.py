# 数字三角形
# 第一遍
# n=int(input())
# a=[]
# for i in range(n):
#     a.append(list(map(int,input().split())))
# dp=[[0]*n for _ in range(n)]
# for i in range(n):
#     for j in range(i+1):
#         if j==0:
#             dp[i][j]=dp[i-1][j]+a[i][j]
#         elif j==i:
#             dp[i][j]=dp[i-1][j-1]+a[i][j]
#         else:
#             dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])+a[i][j]
# print(max(dp[n-1]))
# 第二遍
# n=int(input())
# a=[]
# for i in range(n):
#     a.append(list(map(int,input().split())))
# dp=[[0]*n for i in range(n)]
# for i in range(n):
#     for j in range(i+1):
#         if j==0:
#             dp[i][j]=dp[i-1][j]+a[i][j]
#         elif j==i:
#             dp[i][j]=dp[i-1][j-1]+a[i][j]
#         else:
#             dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+a[i][j]
# print(max(dp[n-1]))
# 第三遍
# n=int(input())
# a=[]
# for i in range(n):
#     a.append(list(map(int,input().split())))
# dp=[[0]*n for i in range(n)]
# for i in range(n):
#     for j in range(i+1):
#         if j==0:
#             dp[i][j]=dp[i-1][j]+a[i][j]
#         elif j==i:
#             dp[i][j]=dp[i-1][j-1]+a[i][j]
#         else:
#             dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+a[i][j]
# print(max(dp[n-1]))
# 第四遍
# n=int(input())
# a=[]
# for i in range(n):
#     a.append(list(map(int,input().split())))
# dp=[[0]*n for i in range(n)]
# for i in range(n):
#     for j in range(i+1):
#         if j==0:
#             dp[i][j]=dp[i-1][j]+a[i][j]
#         elif j==i:
#             dp[i][j]=dp[i-1][j-1]+a[i][j]
#         else:
#             dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])+a[i][j]
# print(max(dp[n-1]))
# 第五遍
# n=int(input())
# a=[]
# for i in range(n):
#     a.append(list(map(int,input().split())))
# dp=[[0]*n for i in range(n)]
# for i in range(n):
#     for j in range(i+1):
#         if j==0:
#             dp[i][j]=dp[i-1][j]+a[i][j]
#         elif j==i:
#             dp[i][j]=dp[i-1][j-1]+a[i][j]
#         else:
#             dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])+a[i][j]
# print(max(dp[n-1]))
a=[1,2,3,5,4]
