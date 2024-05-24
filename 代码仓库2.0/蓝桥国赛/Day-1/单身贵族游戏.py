import os
import sys

# 请在此输入您的代码
a=[['x']*9 for i in range(9)]
for i in range(7):
  n=list(input())
  if len(n)!=7:
    a[i][3]=n[0]
    a[i][4]=n[1]
    a[i][5]=n[2]
  else:
    for j in range(7):
      a[i][j+1]=n[j]
b=[]
for i in range(9):
  for j in range(9):
    if a[i][j]=='1':
      b.append([i,j])
count=0
num=len(b)
for i in range(num):
  if a[b[i][0]-1][b[i][1]]!='1' \
    and a[b[i][0]+1][b[i][1]]!='1'\
          and a[b[i][0]][b[i][1]-1]!='1' \
            and a[b[i][0]][b[i][1]+1]!='1':
    count+=1
if count==num:
  print('yes')
else:
  print('no')