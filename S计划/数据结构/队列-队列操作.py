"""
https://www.lanqiao.cn/problems/1519/learning/
"""
N=int(input())
a=[]
for i in range(N):
    s=list(map(int,input().split()))
    if s[0]==1:
        a.append(s[1])
    elif s[0]==2:
        if a:
            print(a.pop(0))
        else:
            print("no")
    else:
        print(len(a))
