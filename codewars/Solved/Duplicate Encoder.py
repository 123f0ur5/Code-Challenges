def duplicate_encode(word):
    word = word.lower()
    is_dup = set(word)
    dict_dup = {}
    new_word = []
    for x in is_dup:
        dict_dup.update({x : 0})
    for x in word:
        dict_dup[x] += 1
    for x in word:
        if dict_dup[x] > 1:
            new_word.append(')')
        else:
            new_word.append('(')
    new_word = ''.join(new_word)
    return new_word

duplicate_encode('recede')