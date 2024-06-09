#numbers = [1, 2, 3, 4]
'''
numbers = '1234'
letters = ['a', 'b', 'c', 'd']
names = ['Carlos', "Eriberto", 'Rodrigo', 'Pastoriza', 'Ester']
'''
#combo = zip(numbers, letters) When is printed print a zip object
#combo = list(zip(numbers, letters))
#combo = dict(zip(numbers, letters))
'''
combo = list(zip(numbers, letters, names))
'''
#print(combo) 
'''
numbers, letters, names = zip(*combo)
print(numbers, letters, names)
'''

keys = 'Manos a la obra'
values = 'Makikunata llankanchik'

keys = keys.split()
values = values.split()
#print(keys, values)

spanish_kichwa_dict = dict(zip(keys, values))
print(spanish_kichwa_dict)

new_dict = {key:value for key, value in zip(keys, values)}
print(new_dict)

spanish, kichwa = list(spanish_kichwa_dict.keys()), list(spanish_kichwa_dict.values())
print(spanish, kichwa)

spanish_1, kichwa_1 = zip(*spanish_kichwa_dict.items())
print(spanish_1, kichwa_1)

