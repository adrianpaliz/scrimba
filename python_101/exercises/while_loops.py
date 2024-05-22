print('Guessing game')

number_to_guess = 3
index = 0
while index < 3 :
    index += 1
    user_suggestion = int(input('Guess the number, type your beat: '))
    if user_suggestion == number_to_guess:
        print(f'You guessed it')
    else:
        print(f'You didn\'t guessed it')
