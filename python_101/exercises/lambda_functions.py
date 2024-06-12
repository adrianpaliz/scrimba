'''
def function(number): 
    return number + 5
print(function(2))

lambda_function = lambda number: number + 5
print(lambda_function(2))
'''

def strip_spaces(string):
    return ''.join(string.split(' '))
print(strip_spaces('Sueños en la mitad del mundo'))

lambda_string_spaces = lambda string: ''.join(string.split(' '))

print(lambda_string_spaces('Esas no son penas'))

