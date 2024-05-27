n = input()
int_n = int(n)
ans = 0
while int_n > 0:
    s = sum(map(int,list(str(int_n))))
    int_n -= s
    ans += 1
print(ans)
