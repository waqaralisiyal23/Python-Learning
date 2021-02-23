# Generators
# Generators are iterators

# Iterable, Iterator
# iterable pe again and again loop chla skty hain lekin iterator pr ek he bar chla skty hain
l = [1, 2, 3]           # iterable
squares = map(lambda x:x**2, l)           # iterator

# Generator is a sequence like a list but list is iterable and generator is iterator
# now question is that why generators when we have list

# memory ------ [..............................................................]       -> List
# memory ----- (item)   - list poori memory mn store huti hai lkin generator mn ek time pe ek he number memory mn generate
# huga or is se performance bhi achi hugi    -> Generator
# Jab sequence ko bar bar use krna hai tou hum use krengy list lekin agr ek bar he use krna hai tou use krengy generator
# Generator create krna next video/file mn dekhege
