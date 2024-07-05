import random

number_questions = input('How many practice questions do you want?: ')

for index in range(int(number_questions)):
    
    number = random.randint(0, 9)
    number_2 = random.randint(0, 9)
    
    def multiplication():
        answer = input(str(number) + ' X ' + str(number_2) + ' = ')
        result = number * number_2
        results = []
        results.append(str(result))
        print(results)
        def checker():
            correct = 0
            incorrect = 0
            for result in results:
                if result in results:
                    correct += 1
                    print(str(correct))
                else:
                    incorrect += 1
                    print(str(incorrect))
        
        checker() 
    multiplication()
