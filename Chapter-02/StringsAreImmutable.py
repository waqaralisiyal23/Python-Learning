# strings are immutable means ek bar agr string bnali tou wo change ni hu skti 
string="string"
print(string[1])
# string[1]="T" This will give error

print(string.replace("t","T")) #ab ye string change ni hui hai ek ni string create hui hai but original same hai
string.replace("t","T")
print(string) #idhr original string he print hugi replace ek new string bnata hai

new_string=string.replace("t","T")
print(string)
print(new_string)