def quick_sort(q, l, r):
    if l >= r:
        return

    i, j = l - 1, r + 1
    x = q[(l + r) // 2]
    while i < j:
        i += 1
        while q[i] < x:
            i += 1
        j -= 1
        while q[j] > x:
            j -= 1
        if i < j:
            q[i], q[j] = q[j], q[i]
    
    quick_sort(q,l,j)
    quick_sort(q,j+1,r)

n = int(input())
q = list(map(int,input().split()))

quick_sort(q,0,n-1)

print(' '.join(map(str,q)))