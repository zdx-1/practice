s=list(input())
d=""
while s:
    if len(s)==1:
        if d[-1]=="L" and s[0]=="L":
            continue
        else:
            d+="Q"
            s.pop(0)
    else:
        if s[0]==s[1] and s[0]=="L":
            s.pop(0)
        if s[0]!=s[1] and s[0]=="L":
            d+="L"
            s.pop(0)
        if s[0]=="Q":
            d+="Q"
            s.pop(0)
print(d)