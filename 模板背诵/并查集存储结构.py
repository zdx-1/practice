# #第三遍
# Maxn=200
# fa=[]
# def init():
#     for i in range(Maxn+1):
#         fa.append(i)

# init()

# def find(x):
#     if fa[x]==x:
#         return x
#     else:
#         return find(fa[x])
    
# print(find(20))

# def find(x):
#     if fa[x]==x:
#         return x
#     else:
#         fa[x]=find(fa[x])
#         return fa[x]

# print(fa[20])


#第四遍
Maxn=200
fa=[]
def init():
    for i in range(Maxn+1):
        fa.append(i)

def find(x):
    if fa[x]==x:
        return x
    else:
        return find(fa[x])

init()
print(find(20))

def find(x):
    if fa[x]==x:
        return x
    else:
        fa[x]=find(fa[x])
        return fa[x]
print(find(10))