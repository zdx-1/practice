#python集合的一些api
a = set()
for i in range(11):
    a.add(i)   #添加元素
print(a)
a.remove(0)
print(a)
#遍历集合只能用for i in a:
#判断某个元素是否在集合中可以用in关键字
print(0 in a)
a.clear() #清空