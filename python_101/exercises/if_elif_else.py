# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

#Adrián's solution
print("Basic calculator and °C to °F convertor")

value_1 = input("Type a number: ")
operation_sign = input("""What kind of operation you what to perform? 
    Select +, -, * or /. 
    For °C to °F conversion type \"t\": """)
value_2 = input("""Type the second number 
    or leave black in case of conversion to °F: """)

if operation_sign == "+" :
    print(int(value_1) + int(value_2))
elif operation_sign == "-":
    print(int(value_1) - int(value_2))
elif operation_sign == "*":
    print(int(value_1) * int(value_2))
elif operation_sign == "/":
    print(int(value_1) / int(value_2))
elif operation_sign == "t":
    print(((int(value_1)*9)/5) + 32)
else:
    print("Choose a correct operation sign")

#Teacher's solution
'''
mode = input('Enter math operation(+,-,*,/) or f for Celsius to Fahrenheit conversion: ')
num1 = float(input('Enter first number: '))
if mode.lower() == 'f':
    print(f'{num1} Celsius is equivalent to {(num1*9/5)+32} Fahrenheit')
else:
    num2 = float(input('Enter second number: '))

    if mode == '+':
        print(f'Answer is: {num1 + num2}')
    elif mode == '-':
        print(f'Answer is: {num1 - num2}')
    elif mode == '*':
        print(f'Answer is: {num1 * num2}')
    elif mode == '/':
        print(f'Answer is: {num1 / num2}')
    else:
        print('Input error')
'''
