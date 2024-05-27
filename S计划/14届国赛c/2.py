import os
import sys

# 请在此输入您的代码
import math

count = 0

for i in range(1, 1000001):
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            if sorted(str(i)) == sorted(str(j) + str(i // j)):
                count += 1
                break
    if i % 100000 == 0:
        print(i, count)

print(count)
print(590)
