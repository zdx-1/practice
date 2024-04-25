def find0(a):
  for i in a:
    if 0==i:
      global cnt
      cnt+=1
  return cnt
cnt=0
t=int(input())
for i in range(t):
  n=int(input())
  a=list(map(int,input().split()))
  print(find0(a))
  cnt=0
