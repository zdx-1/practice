def partition(a,left,right):
    index=left+1
    for i in range(left+1,right+1):
        if a[i]<a[left]:
            a[i],a[index]=a[index],a[i]
            index+=1
    a[left],a[index-1]=a[index-1],a[left]
    return index-1
def quickSort(a,left,right):
    if left<right:
        mid=partition(a,left,right)
        quickSort(a,left,mid-1)
        quickSort(a,mid+1,right)
a=[5,2,3,1,4]
quickSort(a,0,len(a)-1)
print(a)
