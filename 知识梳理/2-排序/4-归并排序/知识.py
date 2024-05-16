"""
归并排序：
步骤：
1.将待排序数组分成两个子数组，直到每个子数组只有一个元素
2.将两个子数组合并成一个有序数组
3.重复步骤2，直到整个数组有序

时间复杂度：O(nlogn)
空间复杂度：O(n)
稳定性：不稳定

输入：
9
2 8 7 1 3 5 6 4 9
"""
n=int(input())
a=list(map(int,input().split()))
def Merge(A,B):
    result=[]
    while len(A)!=0 and len(B)!=0:
        if A[0]<=B[0]:
            result.append(A.pop(0))
        else:
            result.append(B.pop(0))
    result.extend(A)
    result.extend(B)
    return result
def MergeSort(A):
    if len(A)<2:
        return A
    mid=len(A)//2
    left=MergeSort(A[:mid])
    right=MergeSort(A[mid:])
    return Merge(left,right)
print(' '.join(map(str,MergeSort(a))))