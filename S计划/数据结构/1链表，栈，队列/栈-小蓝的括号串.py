"""
https://www.lanqiao.cn/problems/2490/learning
"""
n=int(input())
s=input()
a=[]
ok=True
for c in s:
    if c == '(':
        a.append(c)
    else:
        if len(a) == 0:
            ok = False
            break
        a.pop()
if ok and len(a) == 0:
    print('Yes')
else:
    print('No')

    