print('python101 - Enumerate')

friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']

'''
index = 1
for friend in friends:
    print(index, friend)
    index += 1
'''

for num, friend in enumerate(friends, 51):
    print(num, friend)

#Print the separate tuples
for friend in enumerate(friends, 51):
    print(friend)

for friend in enumerate(enumerate(friends, 51), -100):
    print(friend)

for num, letter in enumerate('python', start = 5):
    print(num, letter)


print(type(enumerate(friends)))
print(list(enumerate(friends)))


