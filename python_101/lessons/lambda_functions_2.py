'''
def function(number):
    return number
print(type(function(3)))
'''
'''
def function(number):
    return lambda number_2: number_2*number
doubler = function(2)
print(doubler(3))

quintipler = function(5)
print(quintipler(3))
'''

def price_calc(start_cost, hourly_rate):
    return lambda hours: start_cost + hourly_rate * hours

walkin_cost = price_calc(10,30)
print(walkin_cost(2))

premiun_cost = price_calc(1,25)
print(premiun_cost(2))

print(price_calc(1, 25)(2))

print((lambda a, b, c,: a + b + c)(2, 3, 4))
print((lambda a, b, c = 2: a + b + c)(2, 3, 4))
print((lambda a, b, c = 2: a + b + c)(2, c = 3, b = 4))
print((lambda *args: sum(args))(2, 3, 4, 50))


