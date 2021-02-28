'''
Exercise#1: We have a file 'file6.txt' in which names and salaries are stored like this 'name,salary'  e.g: 'Waqar,100000'. Read this
data and wrtie to another file as "Waqar's salary is 100000"
'''
with open('file6.txt') as rf:
    with open('file7.txt', 'a') as wf:
        for line in rf.readlines():
            name, salary = line.split(',')
            wf.write(f'{name}\'s salary is {salary}')