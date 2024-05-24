t,n = map(int,input().split())

a = [0]*100001      #初始化前缀和数组，记录n边形在范围内可出现的所有边长乘积的次数
path = []           #记录选取的边

def dfs(depth,last_x,mul):    #该dfs用于统计n边形各边之积在1~100000之间出现的次数情况
  '''
  depth:   第几条边
  last_x:  上一条边长
  mul ：    当前边长的总乘积
  '''
  if depth==n:          #若是最后一层，且最小的n-1条边之和大于第n条边。并且所有边的乘积<=上限
    if sum(sorted(path)[:-1])>max(path) and mul<=100000:
      global a
      a[mul]+=1          #找到符合条件的乘积，存到a数组中，记录次数
    return

  for i in range(last_x+1,300):   #可行性剪枝，边长不可相等，从上一条边长处开始枚举
    if i**(n-depth)*mul>100000:   #可行性剪枝，预判若选取剩下的所有边之后，乘积会超过上限，则没必要继续枚举了，直接返回上一层
      return                      
    path.append(i)                #否则记录当次选取的边长
    dfs(depth+1,i,i*mul)          #进入下一层，选下一条边
    path.pop()                    #回溯时清除选取的这条边



dfs(0,0,1)

for i in range(1,len(a)):         #构造前缀和数组
  a[i] += a[i-1]


for i in range(t):
  l,r = map(int,input().split())
  print(a[r] - a[l-1])            #计算区间内的前缀和，即区间内n边形的个数