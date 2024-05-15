import sys
read = sys.stdin.readline

n = int(read())

a = list(map(int,read().split()))

b = [0] * 1000001

for i in a:
    b[i] += 1

for i in range(1,1000001):
    if b[i] > 0:
        while b[i]>0:
            print(i,end=' ')
            b[i] -= 1