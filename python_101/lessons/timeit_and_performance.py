import timeit

def test_1():
    [number for number in range(1, 151) if not any([number % divisor == 0 for divisor in range(2, number)]) and not number == 1]
    return(1)

def test_2():
    [x for x in range(1, 151) if not any([x % y == 0 for y in range(2, x)]) and not x == 1]
    return(1)

def test_3():
    [x for x in range(2, 151) if not any([x % y == 0 for y in range(2, x)])]
    return(1)

def test_4():
    prime_numbers = []
    for possible_prime in range(2, 151):
    #Assume number is prime until shown it is not
        is_prime = True
        for number in range(2, int(possible_prime ** 0.5) + 1):
            if possible_prime % number == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(possible_prime)
    return(1)

print(timeit.timeit('test_1()', globals = globals(), number = 10))
print(timeit.timeit('test_2()', globals = globals(), number = 10))
print(timeit.timeit('test_3()', globals = globals(), number = 10))
print(timeit.timeit('test_4()', globals = globals(), number = 10))

