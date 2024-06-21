"""
https://www.luogu.com.cn/problem/P1217
"""
def is_prime(n):  
    if n < 2:  
        return False  
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:  
            return False  
    return True  
# def is_palindrome(n):  
#     return str(n) == str(n)[::-1]  
# s1, s2 = map(int, input().split())  
# # 只检查范围内的回文数  
# for num in range(s1, s2 + 1):  
#     if is_palindrome(num) and is_prime(num) and num>=5:  
#         print(num)
n=int(10**5)
a=[]
for i in range(1,n+1):
    if is_prime(i):
        a.append(i)
        print(i)
print(a)