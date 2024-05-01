#四舍五入和取整
import math
x = 3.1415926
print(round(x,2))  #保留两位小数
print(math.ceil(x))  #上取整
print(math.floor(x))  #下取整
print(int(x))  #向0取整
 
#math库其他常用api
print(math.sqrt(4))  #开根号函数
print(math.pow(2,4))  #指数函数其实也可以用2**4
print(math.fabs(-1))  #浮点绝对值函数