n = int(input())
a =  list(map(int,input().split()))
tmp = [0 for _ in range(n)]

def merge_sort(a, l, r):
    if l == r:
        return
    mid = (l + r) // 2
    merge_sort(a,l,mid)
    merge_sort(a,mid+1,r)
    i, j, k = l, mid + 1, 0
    # [l,mid],[mid+1,r]
    while i <= mid and j <= r:
        if a[i] < a[j]:
            tmp[k] = a[i]
            k += 1
            i += 1
        else:
            tmp[k] = a[j]
            k += 1
            j += 1
    while i <= mid:
        tmp[k] = a[i]
        i += 1
        k += 1
    while j <= r:
        tmp[k] = a[j]
        j += 1
        k += 1
    for i in range(l,r+1):
        a[i] = tmp[i-l]
        k += 1

merge_sort(a, 0, n-1)

print(' '.join(map(str,a)))