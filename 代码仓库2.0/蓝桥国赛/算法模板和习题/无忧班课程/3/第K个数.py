def find_kth_number(n, k):
    cur = 1
    k = k - 1
    while k > 0:
        steps = cal_steps(n, cur, cur + 1)
        # 10 11
        # 10
        # 1
        if steps <= k:
            cur += 1
            k -= steps
        else:
            cur *= 10
            k -= 1
    return cur

def cal_steps(n, n1, n2):
    steps = 0
    while n1 <= n:
        steps += min(n + 1, n2) - n1
        n1 *= 10
        n2 *= 10
    return steps

n, k = list(map(int,input().split()))
res = find_kth_number(n, k)
print(res)
