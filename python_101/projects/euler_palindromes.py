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

def palindrome_create():
    numbers=('9','8','7','6','5','4','3','2','1','0') # we create a list of the strings we will use
    iterations = 0 # we bring along our trusty iterator
    
    for digit_1 in range(10):
        for digit_2 in range(10):
            for digit_3 in range(10):
                #we create the palindrome string by slicing using the iterators
                palindrome_string = numbers[digit_1] + numbers[digit_2] + numbers[digit_3] + numbers[digit_3] + numbers[digit_2] +numbers[digit_1]  
                palindrome = int(palindrome_string) # typecast string into an integer
                # print(pal_str, palindrome) #debug to check palindromes tested
                
                #lowest number to check against that can generate a higher 
                low_value = int(palindrome / 999) # or //999 floor div gives int as answer 
                # highest possible factor to check, one factor must be lower than this
                high_value = int(palindrome ** 0.5) + 1 # **0.5 is "the square root" of palindrome 
                
                # check if palindrome divisible by any of the numbers between min and max
                for digit in range(low_value, high_value):
                    iterations += 1
                    if palindrome % digit == 0: #check for divisibility, since we are stepping through palindromes in order, as soon as we find one: we are Done! 
                       
                        return 'palindrome:', palindrome, 'digit:',digit, 'palindrome / digit:', 
                        palindrome / digit ,'iterations:',iterations #gives nicer close out of loops

def palindrome_create_2():
    
    iterations = 0 # our trusty iterator
    
    for digit_1 in range(9, 0, -1):
        for digit_2 in range(9, -1, -1):
            for digit_3 in range(9, -1, -1):
                # we create the -palindromes by adding the 'placevalues', 
                # example step 999999 -> 998899 -> 997799 etc but only to 100001 
                palindrome = digit_1 * 100000 + digit_2 * 10000 + digit_3 * 1000 + digit_3 * 100 + digit_2 * 10 + digit_1
                #print(palindrome) #debug
                
                low_value = int(palindrome / 999) # or low_val = palindrome//999 
                high_value = int(palindrome ** 0.5) + 1
                for digit in range(low_value, high_value):
                    iterations += 1
                    if palindrome % digit == 0:
                        
                        return 'palindrome:', palindrome, 'digit:', digit, 'palindrome / digit:', 
                        palindrome / digit, 'iterations:', iterations


#palindrome()
#palindrome_back()
for function in ['palindrome_create', 'palindrome_create_2']:
    runs = 10
    start = time.time()
    for run in range(runs):
        return_value = locals()[function]()
        end = time.time()
    print(return_value, 'Average run-time:', (end - start) / runs)

