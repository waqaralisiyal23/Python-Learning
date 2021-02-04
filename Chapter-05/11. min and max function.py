numbers = [6, 60, 32, 2, 48]
print(min(numbers))                  # gives the smallest number which is 2
print(max(numbers))                 # gives the greatest number which is 60

def greatest_difference(list):
    return max(list)-min(list)
print(greatest_difference(numbers))                 # 60-2 = 58 is the greatest difference