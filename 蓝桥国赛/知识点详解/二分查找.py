#bisect模块：维护一个已排序列表，支持二分查找，二分插入
import bisect

a=[1,2,3,4,5,6,7,8,9]
print(bisect.bisect(a,5))  #返回5在列表中的位置