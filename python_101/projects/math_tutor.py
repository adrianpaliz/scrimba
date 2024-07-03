import random

number_questions = input('How many practice questions do you want?: ')


for index in range(int(number_questions)):
    
    number = random.randint(0, 9)
    number_2 = random.randint(0, 9)
    
    def multiplication():
        correct = 0
        incorrect = 0
        answer = input(str(number) + ' X ' + str(number_2) + ' = ')
        result = number * number_2
        if result == int(answer):
            correct += 1
        else:
            incorrect += 1 

    multiplication()

print('Thanks for playing, have a nice day.\n' 'Your correct answers were ' + str(correct))



