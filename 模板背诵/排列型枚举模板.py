"""
        排列型枚举是n个的全排列,就是从n个中选取n个,然后按顺序输出
！！！需要注意的是，相比较组合只关心有多少个集合，而排序是关心集合内的排序方式！！！
"""
order=[0]*20
chosen=[0]*20
n=0
cnt=0
def calc(x):
    if x==n+1:
        ansTemp=''
        for i in range(1,n+1):
            print(order[i],end=' ')
        print()
        global cnt
        cnt+=1
        return
    for i in range(1,n+1):
        if chosen[i]==1:
            continue
        order[x]=i
        chosen[i]=1
        calc(x+1)
        chosen[i]=0
        order[x]=0
n=int(input())
calc(1)
print(cnt)