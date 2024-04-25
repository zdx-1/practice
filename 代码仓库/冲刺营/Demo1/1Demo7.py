#纸张尺寸
l=1189
w=841
i=0
s=input()
n=int(s[-1])
for i in range(n):
    l,w=w,l//2
print(l)
print(w)