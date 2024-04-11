#N皇后问题
x=[0]*5
n=0
sum=0
def pd(k):
    for i in range(1,k):
        if abs(k-i)==abs(x[k]-x[i]):
            print("i={0},k={1}".format(i,k))
            print("\033[35m{1}{0}\033[0m".format(x,k))
            return 0
        elif x[k]==x[i]:
            return 0
    return 1
def check(a):
    if a>n:
        global sum
        sum+=1
        print("\033[38m{0}\033[0m".format(x))
    else:
        return False
    return True
def DFS(a):
    print("\033[34m{1}{0}\033[0m".format(x,a))
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