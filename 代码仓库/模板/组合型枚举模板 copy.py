chosen=[]
n=0
m=0
cnt=0
def calc(x):
    if len(chosen)>m:
        return
    if len(chosen)+n-x+1<m:
        return
    if x==n+1:
        for i in chosen:
            print(i,end=' ')
        print()
        return
    chosen.append(x)
    calc(x+1)