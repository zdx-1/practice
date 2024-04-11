# #第一遍
# order=[0]*20
# chosen=[0]*20
# n=0
# cnt=0

# def calc(x):
#     if x==n+1:
#         ansTemp=""
#         for i in range(1,n+1):
#             print(order[i],end=" ")
#         print()
#         global cnt
#         cnt+=1
#         return
#     for i in range(1,n+1):
#         if chosen[i]==1:
#             continue
#         order[x]=i
#         chosen[i]=1
#         calc(x+1)
#         chosen[i]=0
#         order[x]=0
# n=int(input())
# calc(1)
# print(cnt)

# #第二遍
# order=[0]*20
# chosen=[0]*20
# n,cnt=0,0
# def calc(x):
#     print("\033[32mn+1=={2},x={3},\norder={0},\nchosen={1}\033[0m".format(order,chosen,n+1,x))
#     if x==n+1:
#         ansTemp=""
#         for i in range(1,n+1):
#             print(order[i],end=" ")
#         print()
#         global cnt
#         cnt+=1
#         print("\033[31mn+1=={2},x={3},\norder={0},\nchosen={1}\033[0m".format(order,chosen,n+1,x))
#         return
#     for i in range(1,n+1):
#         if chosen[i]==1:
#             continue
#         order[x]=i
#         chosen[i]=1
#         calc(x+1)
#         chosen[i]=0
#         order[x]=0
#         print("\033[34morder=\033[0m",order)
#         print("\033[38mchosen=\033[0m",chosen)

# n=int(input())
# calc(1)
# print(cnt)


# #第三遍
# order=[0]*20
# chosen=[0]*20
# n=0
# cnt=0
# def calc(x):
#     if x==n+1:
#         ansTemp=""
#         for i in range(1,n+1):
#             print(order[i],end="")
#         print()
#         global cnt
#         cnt+=1
#         return
#     for i in range(1,n+1):
#         if chosen[i]==1:
#             continue
#         order[x]=i
#         chosen[i]=1
#         calc(x+1)
#         chosen[i]=0
#         order[x]=0
# n=int(input())
# calc(1)
# print(cnt)

# #第四遍
# order,chosen=[0]*20,[0]*20
# n,cnt=0,0
# def calc(x):
#     if x==n+1:
#         ansTemp=""
#         for i in range(1,n+1):
#             print(order[i],end='')
#         print()
#         global cnt
#         cnt+=1
#         return
#     for i in range(1,n+1):
#         if chosen[i]==1:
#             continue
#         order[x]=i
#         chosen[i]=1
#         calc(x+1)
#         chosen[i]=0
#         order[x]=0
# n=int(input())
# calc(1)
# print(cnt)

# #第五遍
# order=[0]*20
# chosen=[0]*20
# n=0
# cnt=0
# def calc(x):
#     if x==n+1:
#         for i in range(1,n+1):
#             print(order[i],end="")
#         print()
#         global cnt
#         cnt +=1
#         return
#     for i in range(1,n+1):
#         if chosen[i]==1:
#             continue
#         order[x]=i
#         chosen[i]=1
#         calc(x+1)
#         chosen[i]=0
#         order[x]=0
# n=int(input())
# calc(1)
# print(cnt)


# #第六遍
# order=[0]*20
# chosen=[0]*20
# n=0
# cnt=0

# def calc(x):
#     if x==n+1:
#         for i in range(1,n+1):
#             print(order[i],end="")
#         print()
#         global cnt
#         cnt+=1
#         return
#     for i in range(1,n+1):
#         if chosen[i]==1:
#             continue
#         chosen[i]=1
#         order[x]=i
#         calc(x+1)
#         chosen[i]=0
#         order[x]=0
# n=int(input())
# calc(1)
# print(cnt)


#第七遍
# order=[0]*20
# chosen=[0]*20
# n=0 
# cnt=0

# def calc(x):
#     if x==n+1:
#         for i in range(1,n+1):
#             print(order[i],end="")
#         print()
#         global cnt 
#         cnt+=1
#         return
#     for i in range(1,n+1):
#         if chosen[i]==1:
#             continue
#         order[x]=i
#         chosen[i]=1
#         calc(x+1)
#         order[x]=0
#         chosen[i]=0
# n=int(input())
# calc(1)
# print(cnt)


#第八遍
chosen=[0]*20
order=[0]*20
n=0
cnt=0

def calc(x):
    if x==n+1:
        for i in range(1,n+1):
            print(order[i],end="")
        print()
        global cnt 
        cnt +=1
        return 
    
    for i in range(1,n+1):
        if chosen[i]==1:
            continue
        chosen[i]=1
        order[x]=i
        calc(x+1)
        chosen[i]=0
        order[x]=0

n=int(input())

calc(1)
print(cnt)