numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Standar for loop
'''
new_list = []
Standar for loop
for number in numbers:
    new_list.append(number * number)
print(new_list)
'''
#Using list comprehension
'''
new_list = [number * number for number in numbers]
print(new_list)
'''
#Give me a list with number for each number in numbers if number is even
'''
new_list = [number for number in numbers if number % 2 == 0]
print(new_list)
'''
#Using a lambda function
'''
new_list = filter(lambda number: number % 2 == 0, numbers)
print(list(new_list))
'''

#I want a (letter, num) pair for each letter in 'spam' and each number in '0123'
new_list = []
for letter in 'spam':
    for number in range(4):
        new_list.append((letter, number))
print(new_list)
#Usin list comprehension
new_list = [(letter, number) for letter in 'spam' for number in range(4)]
print(new_list)


