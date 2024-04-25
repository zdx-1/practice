def judge(pushed, poped):  
    stack = []
    push = 0  
    popo = 0  
    while push < len(pushed) and popo < len(poped):   
        stack.append(pushed[push])  
        push += 1   
        while stack and stack[-1] == poped[popo]:  
            stack.pop()  
            popo += 1  
    return push == len(pushed) and popo == len(poped) and not stack  
q = int(input())  
for _ in range(q):  
    n = int(input())  
    pushed = list(map(int, input().split()))  
    poped = list(map(int, input().split()))  
    print("Yes" if judge(pushed, poped) else "No")