
d={}
def find(i):
    temp=list(str(i))
    cnt=0
    for j in temp:
        if j=="0" or j=="6" or j=="9":
            cnt+=1
        if j=="8":
            cnt+=2
    if cnt>0:
        # d.update({cnt:i})
        # d[cnt]=i
        d[i]=cnt
a,b=map(int,input().split())
for i in range(a,b+1):
  find(i)
# print(d[len(d)])
ans=[]
max_cnt=max(d.values())

for k,v in d.items():
    if max_cnt==d[k]:
        ans.append(k)
print(min(ans))
    