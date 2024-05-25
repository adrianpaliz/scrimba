names = ['john ClEEse','Eric IDLE','michael']
names_1 = ['graHam chapman', 'TERRY', 'terry jones']

#My solution
'''
for name in names + names_1:
    print(f'{name.title()}! You are invited to the party on saturday.')

new_names = input('Extra names? Write they down (Separate each name with a comma): ')
names_final = new_names.split(', ')
for name in names_final:
    print(f'{name.title()}! You are invited to the party on saturday')
'''

#Teacher solution
message = 'You are invited to the party on saturday.'

names.extend(names_1)
'''
Or you can use:
names = names + names_1
names += names_1
'''
for index in range(2):
    names.append(input('Enter a new name: '))

for name in names:
    message_1 = f'{name.title()}! {message}'
    print(message_1)

