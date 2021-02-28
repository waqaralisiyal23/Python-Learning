# With Block - Context Manager

with open('file1.txt') as f:
    data = f.read()
    print(data)
print(f.closed)              # returns True because Context Manager khudi file ko close krdeta hai