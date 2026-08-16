def find_multiples_of_three(start, end):
    
    if start > end:
        return []
    
    
    chake = []

    for  num in range(start,end+1):
        if num % 3 == 0:
            chake.append(num)
    return(chake)


print(find_multiples_of_three(1,30))