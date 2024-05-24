# 初始化最后两个斐波那契数（模10）  
last_two = (1, 1)  
# 初始化7的计数器  
count_seven = 0  
  
# 从第三个数开始（因为前两个已经初始化）  
for i in range(3, 202202011201):  
    # 计算下一个斐波那契数（模10）  
    next_fib = (last_two[0] + last_two[1]) % 10  
    # 如果下一个斐波那契数是7，增加计数器  
    if next_fib == 7:  
        count_seven += 1  
    # 更新最后两个斐波那契数  
    last_two = (last_two[1], next_fib)  
  
# 打印7的计数器  
print(count_seven)