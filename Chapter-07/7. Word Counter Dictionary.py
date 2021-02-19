def word_counter(string_):
    count = {}
    string_ = string_.lower()
    for char in string_:
        count[char] = string_.count(char)
    return count
print(word_counter('Waqar Ali Siyal'))