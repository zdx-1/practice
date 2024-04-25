# def kmp(mom_string,son_string):
#     test=""
#     if type(mom_string)!=type(test) or type(son_string)!=type(test):
#         return -1
#     if len(son_string)==0:
#         return 0
#     if len(mom_string)==0:
#         return -1
#     next=[-1]*len(son_string)
#     if len(son_string)>1:
#         next[1]=0
#         i,j=1,0
#         while i<len(son_string)-1:
#             if j==-1 or son_string[i]==son_string[j]:
#                 j+=1
#                 i+=1
#                 next[i]=j
#             else:
#                 j=next[j]
#     m=s=0
#     while s<len(son_string) and m<len(mom_string):
#         if s==-1 or mom_string[m]==son_string[s]:
#             m+=1
#             s+=1
#         else:
#             s=next[s]

#     if s==len(son_string):
#         return m-s
#     return -1

# mom_string="ababababcacccccabca"
# son_string="abca"

# print(kmp(mom_string,son_string))



# #第二遍
# def kmp(mom_string,son_string):
#     test=""
#     if type(mom_string)!=type(test) or type(son_string)!=type(test):
#         return -1
#     if len(son_string)==0:
#         return 0
#     if len(mom_string)==0:
#         return -1
#     next=[-1]*len(son_string)
#     if len(son_string)>1:
#         next[1]=0
#         i,j=1,0
#         while i <len(son_string)-1:
#             if j==-1 or son_string[i]==son_string[j]:
#                 j+=1
#                 i+=1
#                 next[i]=j
#             else:
#                 j=next[j]
#     m=s=0
#     while s<len(son_string) and m<len(mom_string):
#         if s==-1 or mom_string[m]==son_string[s]:
#             m+=1
#             s+=1
#         else:
#             s=next[s]
#     if s==len(son_string):
#         return m-s
#     return -1
# mom_string="123456asddsad"
# son_string="456"
# print(kmp(mom_string,son_string))

# #第三遍

# def kmp(mom_string,son_string):
#     test=""
#     if type(mom_string)!=type(test) or type(son_string)!=type(test):
#         return -1
#     if len(son_string)==0:
#         return 0
#     if len(mom_string)==0:
#         return -1
#     next=[-1]*len(son_string)
#     if len(son_string)>1:
#         next[1]=0
#         i,j=1,0
#         while i<len(son_string)-1:
#             if j==-1 or son_string[i]==son_string[j]:
#                 j+=1
#                 i+=1
#                 next[i]=j
#             else:
#                 j=next[j]
#     m=s=0
#     while m<len(mom_string) and s<len(son_string):
#         if s==-1 or mom_string[m]==son_string[s]:
#             m+=1
#             s+=1
#         else:
#             s=next[s]
#     if s==len(son_string):
#         return m-s
#     return -1
# mom_string="23456a123"
# son_string="123"
# print(kmp(mom_string,son_string))


# #第四遍

# def kmp(momString,sonString):
#     test=""
#     if type(test)!=type(momString) or type(test)!=type(sonString):
#         return -1
#     if len(sonString)==0:
#         return 0
#     if len(momString)==0:
#         return -1
    
#     next=[-1]*len(sonString)
#     if len(sonString)>1:
#         next[1]=0
#         i,j=1,0
#         while i<len(sonString)-1:
#             if j==-1 or sonString[i]==sonString[j]:
#                 i+=1
#                 j+=1
#                 next[i]=j
#             else:
#                 j=next[j]
#     m=s=0
#     while len(sonString)>s and len(momString)>m:
#         if s==-1 or momString[m]==sonString[s]:
#             m+=1
#             s+=1
#         else:
#             s=next[s]
#     if s==len(sonString):
#         return m-s
#     return -1

# mom_string="123456asddsad"
# son_string="456"
# print(kmp(mom_string,son_string))


#第五遍
# def kmp(momStr,sonStr):
#     test=""
#     if type(test)!=type(momStr) or type(test)!=type(sonStr):
#         return -1
#     if len(sonStr)==0:
#         return 0
#     if len(momStr)==0:
#         return -1
#     next=[-1]*len(sonStr)
#     if len(sonStr)>1:
#         next[1]=0
#         i,j=1,0
#         while i<len(sonStr)-1:
#             if j==-1 or sonStr[i]==sonStr[j]:
#                 i+=1
#                 j+=1
#                 next[i]=j
#             else:
#                 j=next[j]
#     m=s=0
#     while s<len(sonStr) and m<len(momStr):
#         if s==-1 or momStr[m]==sonStr[s]:
#             m+=1
#             s+=1
#         else:
#             s=next[s]
#     if s==len(sonStr):
#         return m-s
#     return -1
# momStr="12345678978954612312"
# sonStr="546"
# print(kmp(momStr,sonStr))



# #第六遍
# def kmp(momStr,sonStr):
#     test=""
#     if type(test)!=type(momStr) or type(test) !=type(sonStr):
#         return -1
#     if len(sonStr)==0:
#         return 0
#     if len(momStr)==0:
#         return -1
#     next=[-1]*len(sonStr)
#     if len(sonStr)>1:
#         next[1]=0
#         i,j=1,0
#         while i< len(sonStr)-1:
#             if j==-1 or sonStr[i]==sonStr[j]:
#                 j+=1
#                 i+=1
#                 next[i]=j
#             else:
#                 j=next[j]
#     m=s=0
#     while s<len(sonStr) and m<len(momStr):
#         if s==-1 or momStr[m]==sonStr[s]:
#             m+=1
#             s+=1
#         else:
#             s=next[s]
#     if s==len(sonStr):
#         return m-s
#     return -1
# momStr="12345678965445456315456456"
# sonStr="631"
# print(kmp(momStr,sonStr))


# #第七遍
# def kmp(momStr,sonStr):
#     test=""
#     if type(test)!=type(momStr) or type(test)!=type(sonStr):
#         return -1
#     if len(sonStr)==0:
#         return 0
#     if len(momStr)==0:
#         return -1
    
#     next=[-1]*len(sonStr)

#     if len(sonStr)>1:
#         next[1]=0
#         i,j=1,0
#         while i<len(sonStr)-1:
#             if j==-1 or sonStr[i]==sonStr[j]:
#                 i+=1
#                 j+=1
#                 next[i]=j
#             else:
#                 j=next[j]
#     m=s=0
#     while s<len(sonStr) and m<len(momStr):
#         if s==-1 or momStr[m]==sonStr[s]:
#             m+=1
#             s+=1
#         else:
#             s=next[s]
#     if len(sonStr)==s:
#         return m-s
#     return -1

# momString="12345654123123"
# sonString="54"
# print(kmp(momString,sonString))


# #第八遍
# def kmp(mom,son):
#     test=""
#     if type(test)!=type(mom) and type(test)!=type(son):
#         return -1
#     if len(son)==0:
#         return 0
#     if len(mom)==0:
#         return -1
#     next=[-1]*len(son)
#     if len(son)>1:
#         next[1]=0
#         i,j=1,0
#         while i<len(son)-1:
#             if j==-1 or son[i]==son[j]:
#                 i+=1
#                 j+=1
#                 next[i]=j
#             else:
#                 j=next[j]
#     m=s=0
#     while s<len(son) and m<len(mom):
#         if s==-1 or mom[m]==son[s]:
#             m+=1
#             s+=1
#         else:
#             s=next[s]
#     if s==len(son):
#         return m-s
#     return -1
# mom="12345698123123"
# son="98"
# print(kmp(mom,son))



#第九遍
def kmp(mom,son):
    test=""
    if type(test)!=type(mom) or type(test)!=type(son):
        return -1
    if len(son)==0:
        return 0
    if len(mom)==0:
        return -1
    next=[-1]*len(son)
    if len(son)>1:
        next[1]=0
        i,j=1,0
        while i<len(son)-1:
            if j==-1 or son[i]==son[j]:
                i+=1
                j+=1
                next[i]=j
            else:
                j=next[j]
    m=s=0
    while s<len(son) and m<len(mom):
        if s==-1 or mom[m]==son[s]:
            s+=1
            m+=1
        else:
            s=next[s]
    if s==len(son):
        return m-s
    return -1
mom="12345"
son="45"
print(kmp(mom,son))
    