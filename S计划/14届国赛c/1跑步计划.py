ans = 0
import datetime
start = datetime.datetime(2023, 1, 1)
while start.year == 2023:
    if "1" in start.strftime("%m%d%w"):
        ans += 4
    ans += 1
    start += datetime.timedelta(days=1)
print(ans)
