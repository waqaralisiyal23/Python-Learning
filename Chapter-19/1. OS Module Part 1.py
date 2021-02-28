import os

print(os.getcwd())           # gives the current working directory
# os.mkdir('Movies')         # creates a new folder with a name movies
# os.mkdir('Movies')         # if we create again then it will give error because file already exists therefore first check
if os.path.exists('Movies'):         # current folder mein check krne ke liye poora path dene ki need ni
    print('Movies folder already exists')
else:
    os.mkdir('Movies')

open('file.txt', 'a').close()          # To create a file

# To work with a folder/files in different directory then there are two ways
# os.mkdir(r'D:\Youtube\FolderName')     # first way
# second way
# os.chdir(r'D:\Youtube')      # change the directory then you can directly work with folder/files without giving complete path
# os.mkdir(r'D:\Youtube\FolderName')

print(os.listdir())         # gives the files and folders inside the current working directory

for item in os.listdir():
    path = os.path.join(os.getcwd(), item)        # Joins two paths using '\'
    print(path)
