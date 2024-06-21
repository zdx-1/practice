import bisect
a=[12,34,56,876,45,543]
idx=bisect.bisect_left(a,1234)
print(idx)