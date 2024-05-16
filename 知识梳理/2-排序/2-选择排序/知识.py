"""
选择排序：
选择排序的基本思想是：
在未排序序列中找到最小（大）元素，
存放到排序序列的起始位置，
直到所有元素均排序完毕。
选择排序是不稳定的排序方法，也就是说，
如果两个待比较元素中，有多个元素相等，
那么选择排序是不确定元素顺序的。
时间复杂度：O(n^2)
空间复杂度：O(1)
稳定性：稳定
输入：
9
2 4 6 8 10 1 3 5 7
"""
n=(int(input()))
a=list(map(int,input().split()))
for i in range(n-1):
    min_value=a[i]
    min_index=i
    for j in range(i,n):
        if a[j]<min_value:
            min_value=a[j]
            min_index=j
    a[i],a[min_index]=a[min_index],a[i]

print(" ".join(map(str,a)))