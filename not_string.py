def not_string(word):
    x = word.split()
    if "not" in word:
        return word
    else:
        word = "not " + word
        return word

print(not_string("not bad"))

