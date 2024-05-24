#python列表的一些api
a = [0,1,2,3]
a.insert(0,-1) #i的位置插入b insert(i,b)
print(a)
a.remove(-1)  #删除列表中第一个值为num的数 ,如果找不到会报错
print(a)
print(-1 in a)
tep = a.pop(0)  #移除并返回索引为i的数
print(tep,a)
tep = a.count(1)  #返回列表中num的数量
print(tep)
b = [[1,2],[3,2],[3,1],[2,0],[2,3],[2,-19]]
def cmp(a):      #自定义排序
    return (a[0],a[1])
b.sort(key=cmp)
print(b)
b.reverse()    #逆序反转
print(b)