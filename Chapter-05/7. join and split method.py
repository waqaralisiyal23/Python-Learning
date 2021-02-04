# split metod
# convert string to list
user_info = 'Waqar Ali Siyal 20'
user_info_to_list = user_info.split()       # splits the string from spaces and converts to list
print(user_info_to_list)                           # output: ['Waqar', 'Ali', 'Siyal', '20']

user_info2 = 'Waqar,Ali,Siyal,20'
user_info_to_list2 = user_info2.split(',')       # splits the string from , and converts to list
print(user_info_to_list2)                               # output: ['Waqar', 'Ali', 'Siyal', '20']

# join method
# convert list to string
user_info_list = ['Waqar', 'Ali', 'Siyal', '20']
user_info_list_to_string = ','.join(user_info_list)
print(user_info_list_to_string)