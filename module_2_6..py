def single_root_words(root_word, *other_words):
    same_word = []
    low_root_word = root_word.lower()
    for word in other_words:
        if low_root_word in word.lower() or word.lower() in low_root_word:
            same_word.append(word)
    return same_word


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
