#第四遍

# a=[i for i in range(1,11)]
# x=3
# low=0
# high=len(a)-1

# while low<high:
#     mid=(low+high+1)//2
#     if a[mid]<=x:
#         low=mid
#     else:
#         high=mid-1
# print(a[high])

# while low<high:
#     mid=(low+high)//2
#     if a[mid]>=x:
#         high=mid
#     else:
#         low=mid+1
# print(a[high],a[low])


#第五遍
# a=[i for i in range(1,11)]
# x=3
# low=0
# high=len(a)-1

# while low<high:
#     mid=(low+high+1)//2
#     if a[mid]<=x:
#         low=mid
#     else:
#         high=mid-1
# print(a[high])

# while low<high:
#     mid=(low+high)//2
#     if a[mid]>=x:
#         high=mid
#     else:
#         low=mid+1
# print(a[high])



#第六遍
# a=list(i for i in range(1,11))
# x=4
# low=0
# high=len(a)-1
# # while low<high:
# #     mid=(low+high)//2
# #     if a[mid]>=x:
# #         high=mid
# #     else:
# #         low=mid+1
# # print(a[high])
# while low<high:
#     mid=(low+high+1)//2
#     if a[mid]<=x:
#         low=mid
#     else:
#         high=mid-1
# print(a[high])


#第七遍
# a=list(i for i in range(1,11))
# x=3
# low=0
# high=len(a)-1

# while low<high:
#     mid=(low+high+1)//2
#     if a[mid]<=x:
#         low=mid
#     else:
#         high=mid-1
# print(a[high])

# while low<high:
#     mid=(low+high)//2
#     if a[mid]>=x:
#         high=mid
#     else:
#         low=mid+1
# print(a[high])

# #第八遍
# a=list(i for i in range(1,11))
# x=4
# low=0
# high=len(a)-1

# # while low<high:
# #     mid=(low+high)//2
# #     if a[mid]>=x:
# #         high=mid
# #     else:
# #         low=mid+1
# # print(a[high])

# while low <high:
#     mid=(low+high+1)//2
#     if a[mid]<=x:
#         low=mid
#     else:
#         high=mid-1
# print(a[high])


#第九遍
# a=list(i for i in range(1,11))
# x=2
# low=0
# high=len(a)-1

# while low<high:
#     mid=(high+low)//2
#     if a[mid]<=x:
#         low=mid
#     else:
#         high=mid-1
# print(a[high])

# while low<high:
#     mid=(high+low+1)//2
#     if a[mid]>=x:
#         high=mid
#     else:
#         low=mid+1

# print(a[high])


#第十遍

a=list(i for i in range(1,11))
x=3
low=0
high=len(a)-1

while low<high:
    mid=(low+high+1)//2
    if a[mid]<=x:
        low=mid
    else:
        high=mid-1

print(a[high])

while low<high:
    mid=(low+high)//2
    if a[mid]>=x:
        high=mid
    else:
        low=mid+1

print(a[high])