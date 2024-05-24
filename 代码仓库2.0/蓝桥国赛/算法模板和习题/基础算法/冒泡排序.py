# 冒泡排序
# 时间复杂度：O(n^2),空间复杂度：O(1),稳定
def bubble_sort(alist):
    n = len(alist)
    for j in range(n-1):
        for i in range(n-1-j):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
    return alist
a=[1,3,5,7,9,2,4,6,8,0]
print(bubble_sort(a))