import datetime

time = input().split()
a = [[0, 59], [0, 59], [0, 23], [1, 31], [1, 12]]
for i in range(5):
    if '*' in time[i]:
        time[i] = range(a[i][0], a[i][1] + 1)
    elif '-' in time[i]:
        l, r = map(int, time[i].split('-'))
        time[i] = range(l, r + 1)
    elif ',' in time[i]:
        time[i] = list(map(int, time[i].split(',')))
    else:
        time[i] = [int(time[i])]

s, f, h, d, m = time
days = len(s) * len(f) * len(h)
start = datetime.date(2023, 1, 1)
end = datetime.date(2024, 1, 1)
t = datetime.timedelta(days=1)

cnt = 0
while start < end:
    _, M, D = map(int, str(start).split('-'))
    if M in m and D in d:
        cnt += days
    start += t
print(cnt)
