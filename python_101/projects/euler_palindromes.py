import time

def is_palindrome(value):
    value = str(value)
    if value == value[::-1]:
        return(True)
    else:
        return(False)

# Or we can try
'''
def is_palindrome(value):
    return str(value) == str(value)[::-1]
'''

def palindrome():
    start_time = time.time()
    palindromes_list = []
    debug_list = []
    low_value = 900
    high_value = 999
    iterations = 0

    for number_1 in range(low_value, high_value):
        for number_2 in range(low_value, high_value):
            iterations += 1
            #print(number_1, number_2)
            if is_palindrome(number_1 * number_2):
                palindromes_list.append(number_1 * number_2)
                debug_list.append([number_1, number_2, number_1 * number_2])
            if number_1 == number_2:
                break
    print('print of palindromes:', palindromes_list, number_1, number_2)
    print('debug_list:', debug_list)
    print('Iterations:', iterations)
    print('Largest palindrome:', max (palindromes_list))
    print('Runtime:', time.time() - start_time)
    print('---------End run---------')

def palindrome_back():
    start_time = time.time()
    palindromes_list = []
    debug_list = []
    low_value = 100
    high_value = 999
    iterations = 0
    low_number_2_value = 900

    for number_1 in range(high_value, low_value, -1):
        if number_1 < low_value:
            break
        for number_2 in range(high_value, low_number_2_value, -1):
            iterations += 1
            #print(number_1, number_2)
            if is_palindrome(number_1 * number_2):
                palindromes_list.append(number_1 * number_2)
                low_value = max((number_1 * number_2)/ high_value, low_value)
                low_number_2_value = number_2
                debug_list.append([number_1, number_2, (number_1 * number_2) / high_value, low_value])
            if number_1 == number_2:
                break
    print('print of palindromes:', palindromes_list, number_1, number_2)
    print('debug_list:', debug_list)
    print('Iterations:', iterations)
    print('Largest palindrome:', max (palindromes_list))
    print('Runtime:', time.time() - start_time)
    print('---------End run---------')

palindrome()
palindrome_back()
