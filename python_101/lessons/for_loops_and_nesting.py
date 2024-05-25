'''
for letter in 'Norwegian blue':
    print(letter)
print('For loop done!')
'''

'''
for item in range(8):
    print(item)
print('For loop done!')
'''

'''
for item in range(2, 8):
    print(item)
print('For loop done!')
'''

'''
for item in range(1, 15, 3):
    print(item)
print('For loop from 1 to 15 in step of 3 done!')
'''

'''
for name in ['Guillermo', 'Adrián', 'María', 'Rocio', 'Alejandra']:
    print(name)
print('For loop done!')
'''

'''
friends = ['Guillermo', 'Adrián', 'María', 'Rocio', 'Alejandra']
for friend in friends:
    print(friend)
print('For loop done!')
'''

'''
friends = ['Guillermo', 'Adrián', 'María', 'Rocio', 'Alejandra']
for index in range(len(friends)):
    print(friends[index])
print('For loop done!')
'''

'''
friends = ['Guillermo', 'Adrián', 'María', 'Rocio', 'Alejandra']
for friend in friends:
    if friend == 'María':
        print('Found ' + friend + '!')
        break
    print(friend)
print('For loop done!')
'''

'''
friends = ['Guillermo', 'Adrián', 'María', 'Rocio', 'Alejandra']
for friend in friends:
    if friend == 'María':
        print('Found ' + friend + '!')
        continue
    print(friend)
print('For loop done!')
'''

friends = ['Guillermo', 'Adrián', 'María']
for friend in friends:
    for number in [1, 2, 3]:
        print(friend, number)
print('For loop done!')

