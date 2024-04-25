#在单调递增序列a中查找>=x的数中最小的一个（即x或x的后继）
def findMin(a,x,low,high):
    while low<high:
        mid=int((low+high)/2)
        if(a[mid]>=x):
            high=mid
        else:
            low=mid+1
    print(a[high])
#在单调递增序列a中查找<=x的数中最大的一个（即x或x的前驱）
def findMax(a,x,low,high):
    while low<high:
        mid=int((low+high+1)/2)
        if(a[mid]<=x):
            low=mid
        else:
            high = mid-1
    print(a[low])

a=[1,2,3,4,5,6,7,8,9,10]
x=3
low=0
high=len(a)-1
findMin(a,x,low,high)
findMax(a,x,low,high)





#第一遍
a=[1,2,3,4,5,6,7,8,9,10]
x=3
low=0
high=len(a)-1

#在单调递增序列中查找>=x的数中最小的一个（x或者x的后继）
while low<high:
    mid=int((low+high)//2)
    if a[mid]>=x:
        high=mid
    else:
        low=mid+1
print(a[low],a[high])

#在单调递增序列中查找<=x的数中最大的一个（x或x的前驱）
while low<high:
    mid=int((low+high+1)//2)
    if a[mid]<=x:
        low=mid
    else:
        high=mid-1
print(a[low],a[high])