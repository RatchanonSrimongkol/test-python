def find_divisors(n):
    if n <= 0:
        return []
    
    chake = []
    for num in range(n):
        boak = num + 1
        if n % boak == 0:
            chake.append(boak)
    return chake

print(find_divisors(20))
