'''
Exercise#03: Define a function that take list of words as argument and returns list with reverse of every element in that list
'''

def reverse_every_word(words_list):
    reversed_words_list =[]
    for word in words_list:
        reversed_words_list.append(word[ : :-1])
    return reversed_words_list

print(reverse_every_word(['Adventure', 'Hello', 'Semester']))