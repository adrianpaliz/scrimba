#My solution
'''
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
'''
#Teacher solution
number_to_guess = 76
assumption_number = 0
guess_limit = 5
number_of_guesses = 0

assumption_number = int(input(f'Guess a number 1 - 100: '))
number_of_guesses += 1
while number_of_guesses < guess_limit:
    
    if assumption_number != number_to_guess:
        number_of_guesses += 1
        if assumption_number > number_to_guess:
            assumption_number = int(input(f'{assumption_number} too high - Guess again 1 - 100: '))
        else:
            assumption_number = int(input(f'{assumption_number} too low - Guess again 1 - 100: '))
    if assumption_number == number_to_guess:
        print(f'You Win! You guessed it: {assumption_number}')
        break

if assumption_number != number_to_guess:
    print(f'Sorry you lose! it was {number_to_guess}')

