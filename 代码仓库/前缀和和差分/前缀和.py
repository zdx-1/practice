a=[1,3,7,5,2]

b=[0]*6
for i in range(len(a)):
    if i==0:
        b[i]=a[i]
    else:
        b[i]=a[i]+b[i-1]
print(b)
#b[2,4]
#[2,4]
cnt=b[4]-b[2-1]
print(cnt)
