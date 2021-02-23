# Function Returning Function (closure) practice

def to_power(p):
    def calculate_power(n):
        return n**p
    return calculate_power

square = to_power(2)
cube = to_power(3)
print(square(5))
print(cube(2))