def count_word_occurrences(words): 

    krang = {}

    for i in words:
        if i in krang:
            krang[i] += 1
        else:
            krang[i] = 1
    return krang

print(count_word_occurrences(['กล้วย','แตงโม','ส้ม','กล้วย','ส้ม']))