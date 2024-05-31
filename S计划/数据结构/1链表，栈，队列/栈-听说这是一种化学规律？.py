"""
https://www.lanqiao.cn/problems/3194/learning
"""
s=input()
s=s.replace('5','')
s=s.replace('7','')
s=s.replace('6','9')
s=list(s)
a=[]
for i,c in enumerate(s):
    if c=='3':
        a.append(i)
    elif c=='4' and len(a)!=0:
        idx=a.pop()
        s[i],s[idx]=s[idx],s[i]
print(''.join(s))