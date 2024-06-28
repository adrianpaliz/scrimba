import random, string

#Generating a random number between 0 and 1 (Not including 1)
#print(random.random())
#Using a for loop to geneerate 5 random numbers
'''
for index in range(5):
    print(random.random())
'''
#To generate a number up to 6 (for exmple)
'''
for index in range(5):
    print(random.random() * 6)
'''
#Another way using uniform() function
'''
for index in range(5):
    print(random.uniform(1, 6))
'''
#Generating random integers
'''
for index in range(5):
    print(random.randint(1, 6))
'''
#Generating random numbers from 1 to 100 with a step of 2
'''
for index in range(5):
    print(random.randrange(1, 100, 2))
'''
#Chosing a random item form a list
#days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
#print(random.choice(days))
#Using sample to generate without duplicates
#print(random.sample(days, 2))
'''
random.shuffle(days)
print(days)
'''
smallcaps = 'abcdefghijklmnopqrstuvwxyz'
largecaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
letters_and_numbers = string.ascii_letters + string.digits
#print(letters_and_numbers)
#Generating a random string
word = ''
for index in range(7):
    word += random.choice(letters_and_numbers)
word_1 = ''.join(random.sample(letters_and_numbers, 7))
word_2 = random.choices(letters_and_numbers, k = 7)
print(word)
print(word_1)
print(word_2)
