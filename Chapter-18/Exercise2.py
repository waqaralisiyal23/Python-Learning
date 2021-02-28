'''
Exercise#02: Read an html file and extract all the links and write to another file. Assume that in one line there is one url.
'''
with open('file8.html', 'r') as webpage:
    with open('file9.txt', 'a') as wf:
        # do kam hu skte hain ek tou start se read kr skte hai or dsra direct body se jo bhtr rhega but yahan start se krege
        for line in webpage.readlines():
            if '<a href=' in line:
                pos = line.find('<a href=')
                first_quote = line.find('\"', pos)
                second_quote = line.find('\"', first_quote+1)
                url = line[first_quote+1:second_quote]
                wf.write(f'{url}\n')