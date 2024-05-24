import sys
read = sys.stdin.readline

def ii():
    return int(read())

def il():
    return list(map(int,read().split()))

t = 1
ans = []
for _ in range(t):
    n, B = il()
    a = il()
    
    sum = 0
    cnt = []
    for i in range(n):
        if a[i] & 1:
            sum += 1
        else:
            sum -= 1
        if sum == 0 and i + 1 < n:
            cnt.append(abs(a[i+1]-a[i]))
    
    cnt.sort()
    ans = 0
    for c in cnt:
        if B >= c:
            B -= c
            ans += 1
        else:
            break
    print(ans)