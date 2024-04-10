def kmp(mom_string,son_string):
    # 传入一个母串和一个子串
    # 返回子串匹配上的第一个位置，若没有匹配上返回-1
    m=s=0#母指针和子指针初始化为0
    while(s<len(son_string) and m<len(mom_string)):
        # 匹配成功,或者遍历完母串匹配失败退出
        if mom_string[m]==son_string[s]:
            m+=1
            s+=1
        else:
            s=next[s]
    
    if s==len(son_string):#匹配成功
        return m-s
    #匹配失败
    return -1