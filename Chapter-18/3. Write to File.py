# w, a, r+

with open('file2.txt', 'w') as f:                   # w mode mn file mn overwrite hujyega or purana data remove hujyega
    f.write('Hello there\n')

with open('file2.txt', 'a') as f:                   # a mode mn file mn overwrite ni huga or new data append hujyega purane ke sath
    f.write('Subscribe my channel')

with open('file3.txt', 'r+') as f:
    # r+ mode mn hum file ko read bhi kr skte hain or write bhi kr skte hain or ye khud file create ni krta isliye file phle se bni hu
    # or new data ko overwrite krega like likha hua hai 'hello there' or please add krna hai tou ye wahan tk overwrite krega jahan tk
    # please poora aye or new data hujyega 'pleasethere'
    # f.write('please')
    # ab agr data ko end mn write krna hai tou hum seek method ke zariye cursor ki position change krke write kr skte hain
    f.seek(len(f.read()))     # cursor ki position end mn chli jyegi
    f.write('Please do it')