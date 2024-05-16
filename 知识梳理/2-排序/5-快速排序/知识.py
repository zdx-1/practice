"""
快速排序：
1. 随机选择一个元素作为基准元素，将数组分成两个部分，一部分比基准元素小，一部分比基准元素大。
2. 递归地对两部分进行快速排序。
时间复杂度：O(nlogn)
空间复杂度：O(nlogn)
稳定性：不稳定
输入：
9
2 8 7 1 3 5 6 4 9
"""

def partition(a,left,right):
    idx=left+1
    for i in range(left+1,right+1):
        if a[i]<a[left]:
            a[i],a[idx]=a[idx],a[i]
            idx+=1
    a[left],a[idx-1]=a[idx-1],a[left]
    return idx-1
def quickSort(a,left,right):
    if left<right:
        mid=partition(a,left,right)
        quickSort(a,left,mid-1)
        quickSort(a,mid+1,right)

n=int(input())
a=list(map(int,input().split()))
quickSort(a,0,n-1)
print(" ".join(map(str,a)))