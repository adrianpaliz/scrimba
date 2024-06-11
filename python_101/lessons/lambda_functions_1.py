'''
def square(number):
    return number*number
print(square(3))
'''

'''
square = lambda number: number*number
print(square(4))
'''

'''
def square(number): return number*number
print(square(2))
'''

'''
double_mult = lambda number, number_2: 2*number*number_2
print(double_mult(2,3))
'''

'''
def name_and_alias(name, alias):
    return name.strip().title() + ':' + alias.strip().title()
print(name_and_alias(' john CLEEse ', 'HECKLER'))
'''

'''
name_and_alias = lambda name, alias: name.strip().title() + ':' + alias.strip().title()
print(name_and_alias(' john CLEEse ', 'HECKLER'))
'''
'''
#One line function definition
def name_and_alias(name, alias): return name.strip().title() + ':' + alias.strip().title()
print(name_and_alias(' john CLEEse ', 'HECKLER'))
'''

que_tan_lejos_cast = ['Pancho Aguirre', 'Tania Martinez', 'Cecilia Vallejo', 'Elena Torres', 'Alfredo Espinoza', 'Ricardo Gonzalez']
'''
que_tan_lejos_cast.sort(key = lambda name:name.split(' ')[-1])
print(que_tan_lejos_cast)
'''
def sort_names(name):
    return name.split(' ')
que_tan_lejos_cast.sort(key = sort_names)
print(que_tan_lejos_cast)






