'''
Exercise#02: Take input from user and store in dictionary
'''
user_info = {}
name = input('Enter your name: ')
age = int(input('Enter your age: '))
fav_movies = input('Enter your favorite movies (separated by comma): ').split(',')
fav_songs = input('Enter your favorite songs (separated by comma): ').split(',')

user_info['name'] = name
user_info['age'] = age
user_info['fav_movies'] = fav_movies
user_info['fav_songs'] = fav_songs

for key,value in user_info.items():
    print(f'{key} : {value}')