a=[1,2,3,4,5,6]
a.reverse()
print(a)
for i in a[::]:
    print(i,end=" ")
a.sort(reverse=True)#降序排序
print(a)