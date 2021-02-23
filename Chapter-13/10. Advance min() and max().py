# advance min() and max() function

# numbers = [1, 2, 3, 4, 5, 6]
# print(max(numbers))
# print(min(numbers))

# def func(item):
#     return len(item)
names = ['Waqar Ali Siyal', 'Usama', 'Ahmed Ali']
# print(max(names, key=func))
# print(min(names, key=func))
print(max(names, key=lambda item:len(item)))
print(min(names, key=lambda item:len(item)))

students = {
    'waqar' : {'score' : 90, 'age' : 20},
    'usama' : {'score' : 75, 'age' : 18},
    'ahmed' : {'score' : 96, 'age' : 24}
}

students2 = [
    {'name' : 'waqar', 'score' : 90, 'age' : 20},
    {'name' : 'usama', 'score' : 75, 'age' : 18},
    {'name' : 'ahmed', 'score' : 96, 'age' : 24},
]

print(max(students, key = lambda item : students[item].get('score')))
print(max(students2, key = lambda item : item.get('score'))['name'])