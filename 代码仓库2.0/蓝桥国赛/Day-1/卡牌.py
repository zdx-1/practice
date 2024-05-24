from bisect import *
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
mid=bisect_left(a,a[-1]//2)
print(a[mid])