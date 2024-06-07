try:
    number = int(input('Enter a number between 1 and 30: '))
    number_1 = 30 / number
    if number > 30:
        raise ValueError(number)

except ZeroDivisionError as err:
    print(err, "You can't devide by zero!")

except ValueError as err:
    print(err, number, 'Bad Value! not between 1 and 30!')
    
except:
    print('Invalid Input!')

else:
    print('30 divided by', number, 'is: ', 30/number)

finally:
    print('**Thank you for playing!**')

