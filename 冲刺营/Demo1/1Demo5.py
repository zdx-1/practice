#成绩统计
n=int(input())
a=list(int(input()) for _ in range(n))
cnt1=0
cnt2=0
for i in range(n):
  if a[i]>=60:
    cnt1 +=1
  if a[i]>=85:
    cnt2 +=1
print("{:.0f}%".format(cnt1/n*100))
print("{:.0f}%".format(cnt2/n*100))
