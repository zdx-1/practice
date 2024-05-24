from bisect import *

data=[1,2,3,4,5,6,7,8,9,10]
"""
二分查找左边界
"""
#查找大于等于某个值的第一个位置
index=bisect_left(data,5)
print("5 index  "+str(index))

# 获取值而不是索引
value=data[index]
print("5 value  "+str(value))


"""
二分查找右边界
"""
index=bisect_right(data,5)
print("5 index  "+str(index))
value=data[index-1]
print("5 value  "+str(value))