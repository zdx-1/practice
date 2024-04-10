#N皇后问题
x=[0]*15
n=0
sum=0
def pd(k):
    for i in range(1,k):
        if abs(k-i)==abs(x[k]-x[i]):
            return 0
        elif x[k]==x[i]:
            return 0
    return 1
def check(a):
    if a>n:
        global sum
        sum+=1
    else:
        return False
    return True
def DFS(a):
    if check(a):
        return
    else:
        for i in range(1,n+1):
            x[a]=i
            if pd(a):
                DFS(a+1)
            else:
                continue

n=int(input())
DFS(1)
print(sum)