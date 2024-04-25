# """
# 组合型枚举是在n个数中选m个数的组合，求组合的个数
# """
# chosen=[]
# n=0
# m=0
# cnt=0
# def calc(x):
#     if len(chosen)>m:
#         return
#     if len(chosen)+n-x+1<m:
#         return
#     if x==n+1:
#         for i in chosen:
#             print(i,end=' ')
#         print()
#         global cnt
#         cnt+=1
#         return
#     chosen.append(x)
#     calc(x+1)
#     chosen.pop()
#     calc(x+1)
# temp=input().split()
# n=int(temp[0])
# m=int(temp[1])
# calc(1)
# print(cnt)

