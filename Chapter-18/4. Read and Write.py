# file4 ka data read krke file5 mn write krna hai

with open('file4.txt') as rf:
    with open('file5.txt', 'w') as wf:
        wf.write(rf.read())
