# Import modules
import random
from random import randrange
from time import time
# Ask how many questions user wants
number_questions = int(input('How many practice questions do you want?: '))
# Ask user how high the numbers used should be
max_number = int(input('Highest number used in practice?: '))
# Set score start at zero
score = 0
# Set th answer list
answer_list = []
# Start to counting the time 
start = time()
# Loop through number of questions
for index in range(number_questions):    
# Create two random numbers and calc answer
    number_1 = random.randrange(0, max_number + 1)
    number_2 = random.randrange(0, max_number + 1)
    answer = number_1 * number_2
    user_answer = int(input(f'{number_1} X {number_2} = '))
# Capture answer
    answer_list.append(f'{number_1} X {number_2} = {answer} you: {user_answer}')
    if user_answer == answer:
        score += 1
    end = time()
# Output final score
print(f'Thank you for playing! \nYou got {score} out of {number_questions} ({round(score / number_questions * 100)}%) correct in {round(end - start, 1)} seconds ({round((end - start) / number_questions, 1)} seconds / question)')
# Show user the question
for answer in answer_list:
    print(answer)

