#最多吃多少昆虫，max
#dp_s 表示在s情况下吃虫的最大数量
#路径长度N，最多跳K次，
#每次跳a到b格，可以看成跳一次，就是一次转移
#dp[i][j] 表示跳了i次后，当前处在j位置能吃到的最大昆虫数
#dp[0][0]=0
#dp[i][j]=dp[i-1][j_]  a<=j-j_<=b
T=int(input())
INF=10**18
for i in range(T):
    n,A,B,K=map(int,input().split())
    a=[0]+list(map(int,input().split()))
    ans=0
    dp=[[-INF]*(n+1) for i in range(K+1)]
    dp[0][0] = 0
    for i in range(1, K + 1):
        for j in range(1, n + 1):
            for k in range(A, B + 1):
                if j - k < 0:
                    continue
                dp[i][j] = max(dp[i][j], dp[i - 1][j - k] + a[j])
            ans = max(ans, dp[i][j])
    print(ans)