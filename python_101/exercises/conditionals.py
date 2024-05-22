# optimize/shorten the code in the function
# try to reduce the number of conditionals

#Adrián solution

def num_days(month):

    if month == 'jan' or 'mar' or 'may' or 'jul' or 'aug' or 'oct' or 'dec':
        print(f'number of days in {month} is 31')
    elif month == 'feb':
        print(f'number of days in {month} is 28')     
    elif month == 'apr' or 'jun' or 'sep' or 'nov':
        print(f'number of days in {month} is 30')
    
num_days('may')

#Teacher solution
'''
def num_days(month):
    days = 31
    if month in {'apr', 'jun', 'sep', 'nov'}:
        days = 30
    elif month == 'feb':
        days = 28
    print(f'number of days in {month} is {days}')

num_days('jan')
'''
