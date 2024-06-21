n,x=map(int,input().split())
a=list(map(int,input().split()))
if x in a:
    idx=a.index(x)
    a.insert(idx,x)
else:
    idx=len(a)
    for i in a:
        if i>x:
            idx=a.index(i)
            break
    a.insert(idx,x)
print(" ".join(map(str,a)))