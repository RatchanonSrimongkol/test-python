def group_by_unit_digit(numbers):

    krang =[[],[],[],[],[],[],[],[],[],[]]

    for i in numbers:
        har = i % 10
        krang[har].append(i)

    return krang

print(group_by_unit_digit([21, 34, 51, 23, 37, 44, 60, 11, 91, 99]))
