user_info = {
    'name': 'Waqar',
    'age': 20,
    'fav_movies': ['Dummy Movie 1', 'Dummy Movie 2', 'Dummy Movie 3'],
    'fav_tunes': ['Dummy Tune 1', 'Dummy Tune 2'],
}

more_info = {'name': 'Waqar Ali Siyal', 'state': 'Bin Qasim Town', 'hobbies': ['Coding', 'Cricket', 'PUBG']}
# name key already exists so its value will be updated

user_info.update(more_info)
print(user_info)