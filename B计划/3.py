def solve(number):
    factors = []
    while number % 2 == 0:
        factors.append(2)
        number //= 2 
    
    for i in range(3, int(number ** 0.5) + 1, 2): 
        while number % i == 0:
            factors.append(i)
            number //= i
    
    if number > 1:
        factors.append(number)  
    return len(factors)
a=[0,0]
for i in range(2,1000000):
    a.append(solve(i))
print(a)