winning_number = 27
user_input = input("Guess a number between 1 and 100: ")
user_input = int(user_input)
if user_input==winning_number:
    print("You won!!")
else:
    if user_input<winning_number:
        print("Too low")
    else:
        print("Too high")

