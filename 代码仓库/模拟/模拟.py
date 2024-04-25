"""
一般不涉及算法
1，读懂题，理清楚题目流程
2，代码和步骤一一对应：变量名，函数名，函数功能
3，提取重复的部分，写成对应的函数（子模块）
4，按顺序写，分块调试
"""

# """143饮料换购"""
# n=int(input())
# #n表示瓶盖的数量
# ans=n
# while True:
#     # if n>=3:
#     #     n-=3#把三个瓶盖换成饮料
#     #     ans+=1#统计饮料的总和
#     #     n+=1#更新瓶盖的数量
#     #     pass
#     # else:
#     #     break
#     """下面的方法会更快一些"""
#     if n>=3:
#         #n个瓶盖可以换n//3瓶饮料
#         #还剩下n%3个瓶盖
#         #统计饮料的总和
#         ans+=n//3
#         #更新瓶盖的数量
#         n=n//3+n%3
#     else:
#         break
# print(ans)

"""550图像模糊"""
Map=[]
n,m=map(int,input().split())
for i in range(n):
    a=list(map(int,input().split()))
    Map.append(a)
for i in range(n):
    for j in range(m):
        for delta_x in [-1,0,1]:
            for delta_y in [-1,0,1]:
                x=i+delta_x
                y=j+delta_y

