# 快速创建文件夹
import os

def newFold(foldName):
    # 创建文件夹
    os.mkdir(foldName)
    # 获取当前路径
    print(os.getcwd())
    # 获取当前路径下的所有文件
    print(os.listdir(os.getcwd()))
    # 获取当前路径下的所有文件夹
    print(os.listdir(os.getcwd()))
    #获取当前路径下的所有文件及文件夹

for i in range(4,32):
    newFold('Day-'+str(i))