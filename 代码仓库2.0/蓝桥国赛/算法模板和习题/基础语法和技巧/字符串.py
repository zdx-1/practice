#python字符串的一些api
s = 'hello world'
i = s.find('world')  # 查找子字符串在原字符串中的位置
print(i)
s = 'Hello World'
lower_s = s.lower()  # 转换为小写
upper_s = s.upper()  # 转换为大写
print(lower_s,upper_s)   #大小写转换函数（非字母不变）