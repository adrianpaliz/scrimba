#My solution
print('Guessing game')
attempts = 3
number_to_guess = 69
index = 0
while index < attempts:
    user_suggestion = int(input('Guess the number, type your beat: '))
    index += 1
    if user_suggestion == number_to_guess:
        print(f'You guessed it')
        exit()
    else:
        print(f'You didn\'t guessed it')
        if user_suggestion >= 50:
            print(f'You are close! you win 2 more chances')
            attempts += 2
        elif user_suggestion <= 50:
            print(f'You are low!')

