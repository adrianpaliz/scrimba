# Import the modules
import random
from random import randrange
# User start the game with 1000 $
money = 1000
# Define the bag with 10 marbles (6 green and 4 red)
# Replace two marbles 1 green with a black and 1 red with a white
bag = ['red', 'black', 'red', 'green', 'red', 'green', 'red', 'green', 'red', 'white']
# User will have variable number of draws
user_draws = random.randrange(2, 5 + 1)
      
for draw in range(user_draws):
# If user lose half of his money game is over
    if money >= 501:  

# Before each draw user define how much he will bet
        bet = int(input(f'You have {money} \nHow much you whant to bet?: '))
# User draw a random marble from the bag
        random_marble = random.choice(bag)    
# If user draw a green win the same ammount, if he draw a red he lose the amount he bet
        if random_marble == 'green':
            bag.remove('green')
            money += bet
# Print out data as user go along
            print(f'You take a {random_marble} one, you win :) you have {money}')
        if random_marble == 'red':
            bag.remove('red')
            money -= bet
            print(f'You take a {random_marble} one, you lose :( you have {money}')
# A black marble (10X winner) and 1 white (5X loser)
        if random_marble == 'black':
            bag.remove('black')
            money += bet * 10
            print(f'You take a {random_marble} one, you win 10 times your bet :) you have {money}')
        elif random_marble == 'white':
            bag.remove('white')
            money -= bet * 5
            print(f'You take a {random_marble} one, you lose 5 times your bet :( you have {money}')
    else:        
        print(f"You loose half of your money :( you can't keep betting")
        break
# Marbles are replaced into bag after each round

