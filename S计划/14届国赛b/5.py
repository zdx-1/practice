import os
import sys


T = int(input())
for _ in range(T):
    Bags = list(map(int, input().split()))
    cntA, cntB = map(int, input().split())
    VA, VB = map(int, input().split())

    if VA > VB:  # 保证VA的体积比VB的体积小
        # 当第1和第2个背包中A、B的数量确定时
        # 第3个背包慧将优先放体积较小的物品
        cntA, cntB = cntB, cntA
        VA, VB = VB, VA

    ans = 0  # 记录答案
    # 枚举第一个背包中VA的数量
    for i in range(min(cntA, Bags[0] // VA) + 1):
        # 枚举第二个背包中VA的数量
        for j in range(min(cntA - i, Bags[1] // VA) + 1):

            # 1.预处理
            cnt = i + j  # 记录当前物品数量
            RA = cntA - i - j; RB = cntB  # 记录A,B的余数

            # 2.计算第1和第2个背包中物品B的数量
            k1 = min((Bags[0] - i * VA) // VB, RB)
            cnt += k1; RB -= k1  # 更新数据
            k2 = min((Bags[1] - j * VA) // VB, RB)
            cnt += k2; RB -= k2  # 更新数据

            # 3.第3个背包先放A再放B
            k3 = min(Bags[2] // VA, RA); cnt += k3
            cnt += min((Bags[2] - k3 * VA) // VB, RB)

            ans = max(ans, cnt)
    print(ans)
