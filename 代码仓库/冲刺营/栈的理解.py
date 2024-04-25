for i in range(int(input())):
    n=int(input())
    pushed=list(map(int,input().split()))
    poped=list(map(int,input().split()))
    stack = []
    index=0
    for i in pushed:
        stack.append(i)
        while stack and stack[-1]==poped[index]:
            stack.pop()
            index+=1
            if index ==len(poped):
                break
    print("Yes") if not stack and index==len(poped) else print("No")