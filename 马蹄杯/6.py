L,R=map(int,input().split())
cnt=0
for i in range(L,R+1):
    if "2" in str(i):
        a=list(str(i))
        cnt+=a.count("2")
print(cnt)