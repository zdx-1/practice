def dfs(x, y):  
    # 记忆化搜索的字典  
    global memo  
    # 如果已计算过，则直接返回结果  
    if (x, y) in memo:  return memo[(x, y)]  
    # 当操作队列里没有了，就只有一种方案  
    if x == 0:  return 1  
    # 初始化方案数为0  
    count = 0  
    # 栈里不为空的时候才可以把栈里的元素推出  
    if y > 0:  count += dfs(x, y - 1)  
    # 操作队列里元素减一，栈里元素加一  
    count += dfs(x - 1, y + 1)    
    # 记录方案数并返回  
    memo[(x, y)] = count  
    return count  
  

global memo  
memo = {}  # 初始化记忆化搜索字典  
n = int(input())  
print(dfs(n, 0))  