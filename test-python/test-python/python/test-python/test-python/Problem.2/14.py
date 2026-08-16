def collect_unique_words():
    
    krang = []
    
    while len(krang) < 5 :
        new = input('พิมคำใหม่-- >')
        
        if new not in krang:
            krang.append(new)
    return krang
            
            
print(collect_unique_words())