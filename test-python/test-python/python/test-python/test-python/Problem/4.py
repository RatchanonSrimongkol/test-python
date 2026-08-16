def calculate_sum_and_average():

    collect_number = []


    for i in range(5):
        boak = i + 1 
        kar = float(input(f'ใส่ค่าลงมาค่าที่ {boak} คือ -->' ))
        collect_number.append(kar)
        
    total = sum(collect_number)
    totals = total / 5

    print(f'sum {total}, average {totals}')
    
calculate_sum_and_average()