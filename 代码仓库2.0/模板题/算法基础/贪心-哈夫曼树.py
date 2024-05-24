"""
1228 小明的衣服
https://www.lanqiao.cn/problems/1228/learning
思路：
    最小堆，每次弹出最小的两个元素，相加，再压入最小堆，直到堆中只有一个元素
    循环次数为n-1
    时间复杂度O(nlogn)
    空间复杂度O(n)
    输入：
        5
        5 1 3 2 1 
    输出：
        25
    如果使用常规思路列表排序，每次都进行排序，时间复杂度O(n^2)，会超时
"""
import heapq
n = int(input())
data = list(map(int, input().split()))
ans = 0
heapq.heapify(data)  # 构建最小堆
while n > 1:
    t1 = heapq.heappop(data)  # 弹出最小元素
    t2 = heapq.heappop(data)  # 弹出第二小元素
    t = t1 + t2  
    ans += t
    heapq.heappush(data, t)  # 将和压入最小堆
    n -= 1  # 次数减一
print(ans)

