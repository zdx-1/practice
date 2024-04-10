from datetime import *
dt1=datetime(1901,1,1)
dt2=datetime(2000,12,31)
print(dt1.weekday())
td=dt2-dt1
print(td.days//7)