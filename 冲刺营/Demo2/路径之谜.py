n = 0
flag = [[0 for i in range(26)] for i in range(27)]
resX = [0 for i in range(1000)]
resY = [0 for i in range(1000)]
resCount = 0
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
def check(x, y):
    global n
    if x == n & y == n:
        # print("check point1")
        for i in range(1, n + 1):
            if (col[i] != 0):
                return False
                # 如果箭靶上的数目不为0，根据逆推，我们通过当前路径得不到箭靶上的结果
        for i in range(1, n + 1):
            if (rol[i] != 0):
                return False
        for i in range(0, resCount):
            x2 = resX[i]
            # x 轴坐标
            y2 = resY[i]
            # y 轴坐标
            sum = n * (x2 - 1) + y2 - 1
            # 通过计算的到为题目要求的坐标系
            print(sum, end=" ")
        return False
        # 成功终止
    else:
        return True  # 继续搜索
        # 关于终止还是继续我们交给判定即可
def pd(x2, y2):
    global n
    # print("x2 :", x2,"y2 :", y2, " n ", n)
    if flag[x2][y2] == 1:
        # print("checkPoint3")
        return False
        # 已被走过，不能再走，超出边界
    elif x2 < 1:
        # print("checkPoint5")
        return False
    # 从左侧走出方格
    elif x2 > n:
        # print("checkPoint6")
        return False
    # 从右侧走出方格
    elif col[x2] <= 0:
        # print("checkPoint8")
        return False
    # 没走到右下角，箭用完了
    elif y2 < 1:
        # print("checkPoint7")
        return False
    # 从上侧走出方格
    elif y2 > n:
        # print("y2 :",y2," n ",n)
        return False
    # 从下侧走出方格
    elif rol[y2] <= 0:
        # print("checkPoint9")
        return False
    # 没走到右下角，箭用完了
    else:
        return True
# 符合边界条件，可以继续执行搜索
def dfs(x, y):
    if not check(x, y):
        return
    # 包含不符合规则的地方，回溯，用于剪枝
    else:
        for i in range(0, 4):
            xt = dx[i] + x
            yt = dy[i] + y
            # print(xt, yt)
            if not pd(xt, yt):
                # print("CheckPoint", xt, yt)
                continue
                # 不符合要求继续换方向搜索
            else:
                # 因为要进行位置转移，我们给它起个名字，叫作案现场
                # 比如向下移动
                col[xt] -= 1
                rol[yt] -= 1
                flag[xt][yt] = 1
                global resCount
                resX[resCount] = xt
                resY[resCount] = yt
                resCount += 1
                # print("---------123-------")
                # print(flag)
                # print("----------------")
                dfs(xt, yt)
                # 搜索回溯后，因为没有找到正确答案，所以要回复作案现场，返回到搜索之前
                resCount -= 1
                flag[xt][yt] = 0
                # print("--------321--------")
                # print(flag)
                # print("----------------")
                col[xt] += 1
                rol[yt] += 1
if __name__ == '__main__':
    n = int(input())
    # print("----------------")
    # print(flag)
    # print("----------------")
    rol = input().split()
    rol = list(map(int, rol))
    rol = [0] + rol
    col = input().split()
    col = list(map(int, col))
    col = [0] + col
    flag[1][1] = 1
    # print("----------------")
    # print(flag)
    # print("----------------")
    col[1] -= 1
    rol[1] -= 1
    resX[resCount] = 1
    resY[resCount] = 1
    resCount += 1
    dfs(1, 1)