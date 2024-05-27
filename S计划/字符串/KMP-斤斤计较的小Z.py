Next = [0] * 1000010
def get_next(T):
    for i in range(1,len(T)):
        j = Next[i]
        while j > 0 and T[i] != T[j]:
            j = Next[j]
        if T[i] == T[j]:
            Next[i + 1] = j + 1
        else:
            Next[i + 1] = 0
def KMP(s,t):
    get_next(t)
    ans = 0
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != t[j]:
            j =  Next[j]
        if s[i] == t[j]:
            j += 1
        if j == len(t):
            ans += 1
            j =  Next[j]
    return ans
t = input()
s = input()
print(KMP(s,t))
