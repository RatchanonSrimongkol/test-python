def is_prime(n):
    
    if n <= 1:
        return False
    
    chake = 0
    
    for i in range(1 , n+1):
        if n % i == 0:
            chake += 1
            
    return chake == 2
    
    



def prime_numbers_in_range(start,end):
    
    krang = []
    
    for i in range(start , end+1):
        if is_prime(i):
            krang.append(i)
            
    rvm = sum(krang)
    return krang, rvm

print(prime_numbers_in_range(10, 20))