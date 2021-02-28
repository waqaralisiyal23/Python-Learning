import os
import shutil

fileiter = os.walk(r'E:\Python\Test Folder')               # returns  a generator object
# ek bar loop chlane pr teen cheezein milengi current_path, folder_names, file_names

for current_path, folder_names, file_names in fileiter:
    print(f'Current Path: {current_path}')
    print(f'Folder Names: {folder_names}')
    print(f'File Names: {file_names}')

# os.rmdir('path here')     # removes the directory if it is empty
# os.makedirs('new/inside_new')      # creates a folder new and another folder inside new which is inside_new
# shutil.rmtree('path here')            # removes the directory even if it is not empty or ye rmtree folder ko delete krke recycle bin mn
# ni bhejega blke permanently delete krdega
# shutil.copytree('path from copy', 'path to paste\foldername')        # copy one folder into another
# shutil.copy('path from copy', 'path to paste\filename')         # copy file from one folder to another
# shutil.move('path from copy', 'path to paste\foldername')       # move folder from one folder to another
# shutil.move('path from copy', 'path to paste\filename')       # move file from one folder to another