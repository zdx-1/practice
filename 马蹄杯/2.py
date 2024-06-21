a=list(map(int,input().split()))
a.sort()
if a[1]+1==a[2] and a[1]-1==a[0]:
    print("TRUE")
else:
    print("FALSE")