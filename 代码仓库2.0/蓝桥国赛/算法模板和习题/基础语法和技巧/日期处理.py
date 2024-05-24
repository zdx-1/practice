from datetime import *
# 日期处理
start_date = datetime(2019, 1, 1) # 开始日期
end_date = datetime(2019, 1, 31) # 结束日期
curren_date = start_date # 当前日期
# 循环遍历日期范围内的每一天
while curren_date <= end_date:
    print(curren_date.strftime('%Y-%m-%d'))
    curren_date += timedelta(days=1)
