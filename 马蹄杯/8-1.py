import bisect
a=[2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728]  
n=int(input())
idxl=bisect.bisect_left(a,n)
idxr=bisect.bisect_right(a,n)
if a[idxl-1]+a[idxr]==n*2:
    print(a[idxl-1])
else:
    print(a[idxr])