"""
303 求解01背包问题
https://www.lanqiao.cn/problems/303/learning
"""
def solve(n,C): 
    # 定义解决函数solve，接受物品数量n和背包容量C作为参数
    for i in range(1,n+1): 
        # 遍历每一个物品
        for j in range(1,C+1): 
            # 遍历每一个背包容量
            if w[i]>j: 
                # 如果当前物品的重量大于背包容量，则不能加入物品
                dp[i][j]=dp[i-1][j] 
                # 继承上一个物品在相同容量下的最优解
            else: 
                # 否则，可以选择加入或不加入当前物品
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-w[i]]+v[i]) 
                # 取加入和不加入当前物品时，价值较大的方案
    return dp[n][C] 
    # 返回最优解，即n个物品在背包容量为C时的最大价值
N = 1001 
# 定义N为物品和背包容量的上限
w=[0]*N 
# 初始化每个物品的重量数组w，大小为N，初始值为0
v=[0]*N 
# 初始化每个物品的价值数组v，大小为N，初始值为0
dp=[[0]*N for i in range(N)] 
# 初始化动态规划表dp，大小为N×N，初始值为0
C,n=map(int,input().split()) 
# 从标准输入接收背包容量C和物品数量n
for i in range(1,n+1): 
    # 遍历每一个物品
    w[i],v[i]=map(int,input().split()) 
    # 从标准输入接收每个物品的重量和价值，并赋值到数组w和v
print(solve(n,C)) 
# 调用solve函数，计算并打印最优解