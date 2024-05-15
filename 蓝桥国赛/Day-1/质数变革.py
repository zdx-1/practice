"""
高效求解质数-- 埃氏筛法
质数的定义：
    在大于 1 的自然数中,除了 1 和它本身以外不再有其他因数的自然数。
因此对于每个数 x,我们可以从小到大枚举 [2,x-1] 中的每个数 y,
判断 y 是否为 xx 的因数。

代码实现：
n = 10**8  # 代求的范围中的最大值
k = 0
s = [True for i in range(n)]  # 首先默认所有数都是质数
z = []
for i in range(2,n):
    if s[i]:  # 判断是否为质数，如果没有被标记过，就是质数
        k+=1
        z.append(i) #添加质数
        for j in range(i+i,n,i):   # 将是指数的倍数的数都改为False
            s[j] = False

print(k) # 个数
print(z) # 质数

"""
from bisect import *
N=1e6+5 # 定义数组的最大大小
a=[0]*N # 存储数字的数组
isPrime=[True]*N # 存储数字是否为素数的数组
G=[[] for _ in range(N)] # 存储因子关系的向量数组
dif=[0]*N # 存储质数之间的差值的数组

# 埃氏筛法求质数
def get_prime(n):
    global Prime
    isPrime[1]=False # 1不是质数
    for i in range(2,n+1):
        if isPrime[i]: # 如果是质数
            Prime.append(i) # 添加到质数数组
        for j in range(len(Prime)):
            if Prime[j]*i>n: # 如果大于n，则退出循环
                break
            isPrime[Prime[j]*i]=False # 否则标记为非质数
            if i%Prime[j]==0: # 如果能整除，则退出循环
                break