def check_prime(n):
    if n <= 1:
        return "is not prime"

    divisors = []
    for num in range(n):
        boak = num + 1
        if n % boak == 0:
            divisors.append(boak)
    
    if len(divisors) == 2:
        return "is prime"
    else:
        return "is not prime"
    
print(check_prime(17))
print(check_prime(18)) 
