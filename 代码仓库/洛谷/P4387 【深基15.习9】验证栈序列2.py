q=int(input())
for _ in range(q):
    n=int(input())
    pushed=list(map(int,input().split()))
    poped=list(map(int,input().split()))
    stack = []
    push_index=0
    pop_index=0
    while push_index < len(pushed) and pop_index <len(poped):
        stack.append(pushed[push_index])
        push_index +=1
        while stack and stack[-1]==poped[pop_index]:
            stack.pop()
            pop_index += 1
    if push_index == len(pushed) and pop_index ==len(poped) and not stack:
        print("Yes")
    else:
        print("No")