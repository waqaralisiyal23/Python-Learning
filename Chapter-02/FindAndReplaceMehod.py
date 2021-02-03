#replace() method
string="she is beautiful and she is good dancer"
print(string.replace(" ","_"))
print(string.replace("is","was"))
#ar sirf first is ko change krna hai tou 1 deny ya phle do is ko change krna hai tou 2 or teen k liye 3
# r sab change krne k liye bs srf replace("is","was")
print(string.replace("is","was",1))

# find() method: To find the index of a word or a character in a string
print(string.find("is"))
string="is she is beautiful and she is good dancer"
print(string.find("is"))
#ab pehleis ki maloom ni krni dsre ki krni tou hum search kaha se start kre wo argumet dengy
print(string.find("is",1)) # 1index se find krna shroo krega
string="she is beautiful and she is good dancer"
#ab dsre is ki maloom krni lekin supose first is ki ni pata tou uske agy se kese search shroo kre
is_pos1=string.find("is")
is_pos2=string.find("is",is_pos1+1)
print(is_pos2)

