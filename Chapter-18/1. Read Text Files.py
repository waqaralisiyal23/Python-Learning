# readfile
# open function
# read method
# seek method
# tell method
# readline method
# readlines method
# close method

f = open('file1.txt')           # read krne ke liye second argument dege r or ni bhi dege by default read mode mn huta hai

print(f'Cursor position: {f.tell()}')          # tell method cursor ki position btata hai
print(f.read())
print(f.read())         # second time read call krege tou kuch print ni huga kiunke hum already read kr chuke hain humara cursor end mn huga
print(f'Cursor position: {f.tell()}')

f.seek(84)              # seek method se hum cursor position change kr skte hain
# ab cursor ko change kiya hai 70 position r hai tou ab phr wahan se read kr skte hain
print(f.read())

f.seek(0)                # wapis cursor ko start mn lane k liye
print(f.readline(), end='')                  # readline ek time mn ek he line read krega
print(f.readline(), end='')

f.seek(0)                   # wapis cursor ko start mn lane k liye
lines = f.readlines()
print(lines)
print(len(lines))
print(lines[0])

# To print all lines using for loop
for line in lines:
    print(line, end='')
print()   # just to change line

print(f.name)               # tells the file name
print(f.closed)             # returns True if file is closed else False

f.close()