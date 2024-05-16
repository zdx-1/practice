"""
插入排序：
1.从第一个元素开始，该元素可以认为已经被排序
2.取出下一个元素，在已经排序的元素序列中从后向前扫描
3.如果该元素（已排序）大于新元素，将该元素移到下一位置
4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
5.将新元素插入到该位置后
6.重复步骤2~5
时间复杂度：O(n^2)
空间复杂度：O(1)
稳定性：稳定
输入：
9
2 4 6 8 1 3 5 7 9
"""
n=int(input())
a=list(map(int,input().split()))
for i in range(1,n):
    value=a[i]
    insert_idx=0
    for j in range(i-1,-1,-1):
        if a[j]>value:
            a[j+1]=a[j]
        else:
            insert_idx=j+1
            break
    a[insert_idx]=value

print(" ".join(map(str,a)))