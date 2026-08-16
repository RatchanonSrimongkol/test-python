def remove_word_from_list(words, word):
    
    if word in words:
        words.remove(word)
    return words



    

print(remove_word_from_list(["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"],'lemon'))
    