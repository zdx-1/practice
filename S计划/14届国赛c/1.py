sun = 0  # 假设这个变量用来累计某种“分数”或“数量”
import datetime

a = datetime.date(2023, 1, 1)

# 遍历2023年的每一天
while a.year == 2023:
    if '1' in a.strftime("%m%d"):  # 检查月份和日期是否包含'1'
        sun += 4  # 如果包含，则加4
    sun += 1  # 每天都加1，不论是否包含'1'
    a += datetime.timedelta(days=1)  # 移动到下一天
print(sun)  # 输出最终累计的“分数”或“数量”

print(a.strftime("%m"))
print(a.strftime("%d"))
