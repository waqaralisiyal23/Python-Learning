# Dictionary Comprehension with if else
# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even', 7: 'odd', 8: 'even', 9: 'odd', 10: 'even'}

odd_even = { num:('even' if num%2==0 else 'odd') for num in range(1, 11)}
print(odd_even)