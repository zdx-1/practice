#同一个位置只能操作一次
def solve():
    t,s=list(input()),list(input())
    ans=0
    for i in range(len(s)):
        if s[i] != t[i]:
            if i>0 and s[i] !=s[i-1] and i<len(s)-1 and s[i]!=s[i+1]:
                ans+=1
                s[i]=t[i]
            else:
                return -1
    return ans
d=int(input())
for _ in range(d):
    print(solve())