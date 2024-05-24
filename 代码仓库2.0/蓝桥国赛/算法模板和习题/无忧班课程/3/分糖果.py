import sys

def ii():
    return int(read())

def il():
    return list(map(int,read().split()))

def read():
    return sys.stdin.readline().strip()

t = 1
ans = []
for _ in range(t):
    n, x = il()
    s = read()
    s = sorted(s)
    if s[0] != s[x-1]:
        # 判断最小字符数量小于x
        print(s[x-1])
        sys.exit(0)
    # 最小字符数量大于等于x
    ans.append(s[0])
    if s[x] != s[n-1]:
        # 说明剩下的不全是一个字符，我们就直接把[x,n-1]所有字符填到ans里
        for i in range(x,n):
            ans.append(s[i])
    else:
        # 剩下的全是一个字符，直接均分
        for i in range((n-1)//x):
            ans.append(s[n-1])
    print(''.join(ans))