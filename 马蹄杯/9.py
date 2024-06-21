import bisect
n,m=map(int,input().split())
a=list(map(int,input().split()))
for i in range(m):
    ch,x=input().split()
    x=int(x)
    if ch=="L":
        if x in a:
            idx=bisect.bisect_left(a,x)
            print(idx)
        else:
            print(-1)
    else:
        if x in a:
            idx=bisect.bisect_right(a,x)
            print(idx)
        else:
            print(-1)