#python中常用的进制转换   转换后的东西一般为字符串需要处理掉前两位
print(bin(7))
print(bin(7)[2:])  #二进制
print(oct(8*8*8-1))
print(oct(8*8*8-1)[2:])  #八进制
print(hex(16*16-1))
print(hex(16*16-1)[:])  #十六进制
 
print(int('111',2))   #二转10
print(int('777',8))   #八转10
print(int('ff',16))   #16转10
 
#字符串可以直接转化为整形和浮点形
a,b = input().split()
print(int(a),float(b))
#ASCLL转整数和整数转ASCLL
print(ord('A')) #ascll转整数
print(chr(65))  #整数转字符
print(str(65))