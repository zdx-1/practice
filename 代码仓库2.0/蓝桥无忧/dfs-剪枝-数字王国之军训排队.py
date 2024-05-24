# 2942
import sys
sys.setrecursionlimit(100000)
n = int(input())

a = list(map(int,input().split()))
ans = n

# 判断当前这个学生是否能进入
def check(x,group):
  for i in group:
    if x % i == 0 or i % x == 0:
      return False
  return True
# 分组
groups = []
def dfs(x):
  # x： 当前是第几个学生
  global ans
  if len(groups) > ans:
    return

  if x == n:
    ans = min(ans,len(groups))
    return
  
  # 枚举当前学生是否能加入到已有的组内
  for i in range(len(groups)):
    if check(a[x],groups[i]):
      groups[i].append(a[x])
      # 当前学生添加进来之后，就要去看下一个学生了
      # 这个地方是回溯，也就是这个学生添加到这个组之后，去看下一个组可不可以
      # 其实就是让当前这个人进去每个组试试
      dfs(x + 1)
      # 回溯删除
      groups[i].pop()
  
  # 这是第二种情况，对于每个人来说，都有单独开一组的权利
  groups.append([a[x]])
  # 一样要回溯
  dfs(x + 1)
  groups.pop()
dfs(0)
print(ans)