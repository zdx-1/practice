def max_increasing_sum(flowers):  
    n = len(flowers)  
    # dp[i] 表示以第 i 朵花结尾的最大递增子序列的和  
    dp = [0] * n  
    dp[0] = flowers[0]  # 第一朵花的能量就是它自己的能量  
    max_sum = dp[0]  # 初始化最大和为第一朵花的能量  
      
    for i in range(1, n):  
        # 初始化当前花的能量为当前的最大值，因为单独一朵花也可以构成递增子序列  
        dp[i] = flowers[i]  
        # 遍历前面的所有花，如果找到能量比当前花小的，那么更新当前花的最大递增子序列和  
        for j in range(i):  
            if flowers[j] < flowers[i]:  
                dp[i] = max(dp[i], dp[j] + flowers[i])  
        # 更新全局最大和  
        max_sum = max(max_sum, dp[i])  
      
    return max_sum  
  
# 从标准输入读取数据  
n = int(input().strip())  
flowers = list(map(int, input().strip().split()))  
  
# 计算最大递增子序列的和  
result = max_increasing_sum(flowers)  
  
# 输出结果  
print(result)