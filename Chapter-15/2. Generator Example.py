# You can create generator using generator function and generator comprehension
# Create your first generator with generator function

# def nums(n):
#     for i in range(1, n+1):
#         print(i)
# nums(10)
def nums(n):
    for i in range(1, n+1):
        yield(i)
# for number in nums(10):
#     print(number)

# memory ---------> 1, jab next number ki demand krege 1 memory se khtm hujyega or next number ayega
# memory ---------> 2 and so on isi trah chlta rhega or ek time mn memory mn ek he number huga

numbers = nums(10)

for number in numbers:
    print(number)
for number in numbers:
    print(number)
# Do bar for loop use kiya hai lekin dsri bar numbers print ni hungy
# We can convert generator to list using list(generator)