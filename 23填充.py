s=input()
n=len(s)
s='?'+s
f=[0]*(n+1)
for i in range(2,n+1):
  if s[i-1]=='?' or s[i]=="?" or s[i]==s[i-1]:
    f[i]=f[i-2]+1
  else:
    f[i]=f[i-1]
print(f[n])