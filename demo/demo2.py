for _ in range(int(input())):
    n=int(input())
    x1=n//4-1
    x2=x1+2
    if n%8==0 and n!=0:
        print("Yes")
        print(x1,x2)
    else:
        print("No")