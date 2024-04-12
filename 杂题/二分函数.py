import bisect
ls=[int(i) for i in range(15)]
index1=bisect.bisect(ls,3)
index2=bisect.bisect_left(ls,4)
index3=bisect.bisect_right(ls,7)
print(ls[index1])
print(ls[index2])
print(ls[index3])

import os
import sys
import math
# 请在此输入您的代码
t=int(input())
for i in range(t):
  print("{:.3f}".format(math.pow(int(input()),1/3)))