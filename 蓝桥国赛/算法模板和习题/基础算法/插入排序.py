# 插入排序
def insertSort(alist):
    for i in range(1,len(alist)):
        temp = alist[i]
        j = i - 1
        while j >= 0 and temp < alist[j]:
            alist[j+1] = alist[j]
            j -= 1
        alist[j+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
insertSort(alist)
print(alist)