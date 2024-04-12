import os
import sys
x1=list(map(int,input().split()))
x2=list(map(int,input().split()))
x3=list(map(int,input().split()))
mix=[[]for i in range(x1[0]+1)]
for i in range(x1[2]):
    a,b,c=map(int,input().split())
    d=(max(x2[a-1],x2[b-1]))
    mix[c].append([a,b,d])

dp=[float("inf") for i in range(x1[0]+1)]
for i in x3:
    dp[i]=0

def dns(i):
    if dp[i] !=float("inf"):
        return dp[i]
    for j in range(len(mix[i])):
        dp[i]=min(dp[i],max(dns(mix[i][j][0])),\
                  dns(mix[i][j][1])+mix[i][j][2])
    return dp[i]
print(dns(x1[3]))