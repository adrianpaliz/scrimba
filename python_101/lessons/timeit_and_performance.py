print([number for number in range(1, 152) if not any([number % divisor == 0 for divisor in range(2, number)]) and not number == 1])

print([x for x in range(1, 151) if not any([x % y == 0 for y in range(2, x)]) and not x == 1])

print([x for x in range(2, 151) if not any([x % y == 0 for y in range(2, x)])])

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
print(prime_numbers)
