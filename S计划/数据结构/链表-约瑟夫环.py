"""
https://www.lanqiao.cn/problems/1111/learning
"""
#在python中不需要自己构建链表，使用list就够用
n,k,m=map(int,input().split())
a=list(range(1,n+1))
i=k-1
while a:
    i=(i+(m-1))%len(a)
    print(a.pop(i))
