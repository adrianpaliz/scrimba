names = ['john ClEEse','Eric IDLE','michael']
names_1 = ['graHam chapman', 'TERRY', 'terry jones']

for name in names + names_1:
    print(f'{name.title()}! You are invited to the party on saturday.')

new_names = input('Extra names? Write they down (Separate each name with a comma): ')
names_final = new_names.split(', ')
for name in names_final:
    print(f'{name.title()}! You are invited to the party on saturday')


