#bisect模块：维护一个已排序列表，支持二分查找，二分插入
from bisect import *

a=[1,2,3,3,3,3,4,5,6,7,8,9]
print("x={},index={}".format(3,bisect_left(a,3))) 
# 从左边开始二分查找，返回找到的第一个3的索引
print("x={},index={}".format(3,bisect_right(a,3)))
# 从左边开始二分查找，返回找到的最后一个3的索引
print("x={},index={}".format(3,bisect(a,3)))
# 从左边开始二分查找，返回找到的最后一个3的索引

insort(a,2)
# 插入2到已排序列表a中
print(a)