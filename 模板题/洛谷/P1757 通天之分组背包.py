m,n=map(int,input().split())
dp=[0]*(m+1)
k=[0]*101
w_v=[]
for i in range(n):
    a,b,c=map(int,input().split())
    w_v.append((a,b))
    k[c]+=1

def solve(wi_vi):
    for j in (m,0,-1):
        for wi,vi in wi_vi:
            if j>=wi:
                dp[j]=max(dp[j],dp[j-wi]+vi)

for i in range(101):
    if k[i]:
        wi_vi=[]
        for i in range(k[i]):
            wi_vi.append(w_v.pop(0))
        solve(wi_vi)
print(dp[-1])

    





# V,N=map(int,input().split())
# dp=[0]*(V+1)
# group=[0]*101
# w_v=[]
# for i in range(1,N+1):
#     wi,vi,ki=map(int,input().split())
#     w_v.append((wi,ki))
#     group[ki]+=1
# w_v_v=[]
# for i in range(101):
#     if group[i]:
#         for i in range(group[i]):
#             w_v_v.append(w_v.pop(0))
#         for j in range(V,0,-1):
#             for w,v in w_v_v:
#                 if j>=w:
#                     dp[j]=max(dp[j],dp[j-w]+v)
                
# print(dp[-1])