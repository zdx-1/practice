#首先就是python不换行输出可以利用,end参数
for i in range(10):
    print("You will Win",end=' ')
#通过上述方法就可以不换行输出以单空格输出了
print()
print("You will get {:.6f}".format(149.999999))
print("You will get %.6lf"%(149.999999))
#格式化输出常采用上述两种方法
#但是也不止是这些，还有join方法
print(",".join(["1","2","3","4","5"]))
