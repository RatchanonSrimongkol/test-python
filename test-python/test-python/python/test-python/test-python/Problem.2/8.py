def separate_by_index(s):
    even_str = ""
    odd_str = ""
    
    for index, char in enumerate(s):
        if index % 2 == 0:
            even_str += char
        else:
            odd_str += char
    
    return even_str, odd_str

print(separate_by_index("Hello World"))