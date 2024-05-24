# 选择排序
# 时间复杂度O(n^2),空间复杂度O(1),稳定
def mysort(alist):
    for i in range(len(alist)-1):
        min_index = i
        min_value = alist[i]
        for j in range(i,len(alist)):
            if alist[j]<min_value:
                min_value = alist[j]
                min_index = j
        # 交换
        alist[i],alist[min_index] = alist[min_index],alist[i]
print("选择排序")
alist = [1,3,5,2,4,6,7,8,9,0]
print(alist)
mysort(alist)
print(alist)