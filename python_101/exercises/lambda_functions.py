#First exercise
'''
def function(number): 
    return number + 5
print(function(2))

lambda_function = lambda number: number + 5
print(lambda_function(2))
'''
#Second exercise
'''
def strip_spaces(string):
    return ''.join(string.split(' '))
print(strip_spaces('Sueños en la mitad del mundo'))

lambda_string_spaces = lambda string: ''.join(string.split(' '))
print(lambda_string_spaces('Esas no son penas'))
'''
#Third exercise
'''
def join_list_no_duplicates(list_a, list_b):
    return list(set(list_a + list_b))
list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6, 7]
print(join_list_no_duplicates(list_a, list_b))

lambda_join_no_duplicates = lambda list_a, list_b: list(set(list_a + list_b))
print(lambda_join_no_duplicates(list_a, list_b))
'''
#Fourth exercise
'''
def create_quad_function(a, b, c):
    return lambda x: a * (x)**2 + b * x +c

f = create_quad_function(2, 4, 6)
g = create_quad_function(1, 2, 3) 
print(f(2))
print(g(2))
'''
#Fifth exercise
signups = ['MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']
print(sorted(signups)) # Lexicographic sort
print(sorted(signups,  key = lambda signups: int(''.join(filter(str.isdigit, signups))))) # Integer sort






