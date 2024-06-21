n=int(input())
flower={}
for i in range(1,n+1):
    s1,s2=input().split()
    if s1 in flower.keys():
        flower[s1]+=int(s2)
    else:
        flower[s1]=1000+int(s2)
res_min=min(flower,key=flower.get)
print(res_min)
print(flower[res_min])