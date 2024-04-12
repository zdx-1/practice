a=[i for i in range(11)]
x=3
low=0
high=len(a)-1
while low<high:
    mid=(low+high+1)//2
    if a[mid]<=x:
        low=mid
    else:
        high=mid-1
print(a[high])

while low<high:
    mid=(low+high)//2
    if a[mid]>=x:
        high=mid
    else:
        low=mid+1
print(a[high])