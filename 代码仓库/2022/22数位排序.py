n = int(input())
m = int(input())
a = [i for i in range(1, n + 1)]
b = [0] * (n + 1)
for i in range(1, n + 1):
    #求i的数位之和
    num = i
    while num != 0:
        b[i] += num % 10
        num //= 10


a.sort(key=lambda x: (b[x], x))
print(a[m - 1])
