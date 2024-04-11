#通过逐个尝试所有可能的值或组合来解决问题的方法
""" 
确定解空间（一维，二维）
确定空间边界（每个变量最小值，最大值，步长）
估算时间复杂度
如果第三步无法通过，通过减少枚举空间，变换枚举顺序等重新从1开始迭代
"""
#百钱买百鸡
#x+y+z=100
#5x+3y+z/3=100
"""
思路：枚举x枚举y枚举z
思路2：枚举x枚举y
思路3：枚举x
"""

# """
# 160字符计数
# """
# s=input()
# cnt=0
# cnt2=0
# for i in s:
#     if i=="aeiou":
#         cnt+=1
#     else:
#         cnt2+=1
# print(cnt)
# print(cnt2)

# """
# 152反倍数
# """
# n=int(input())
# a,b,c=map(int,input().split())
# ans=0
# for i in range(1,n+1):
#     if i%a!=0 and i%b!=0 and i%c!=0:
#         ans+=1
# print(ans)
# """容斥：
# 1-n中a的倍数由n//a个
# 1-n中b的倍数由n//b个
# 1-n中ab的倍数由n//(ab)个
# 1-n中是a或b的倍数由n//a+n//b-n//(ab)
# """


# """
# 153洁净数
# """
# n=int(input())
# ans=0
# for i in range(1,n+1):
#     if "2" not in str(i):
#         ans+=1
# print(ans)


"""
549扫雷
"""
n,m=map(int,input().split())
a=list(list(map(int,input().split())) for i in range(n))
b=[[0]*m for i in range(n)]

dir=[(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
# #方向数组

for i in range(n):
    for j in range(m):
        if a[i][j]:
            b[i][j]=9
        else:
            b[i][j]=0
            for k in range(8):
                x,y=i+dir[k][0],j+dir[k][1]
                if 0<=x<n and 0<=y<m:
                    b[i][j]+=a[x][y]
        print(b[i][j],end=" ")
    print()
