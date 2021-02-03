def greater_of_two(num1, num2):
    if num1>num2:
        return num1
    return num2

def greater_of_three(num1, num2, num3):
    # bigger = greater_of_two(num1, num2)
    # return greater_of_two(bigger, num3)
    return greater_of_two(greater_of_two(num1, num2), num3)

print(greater_of_three(10,20,30))