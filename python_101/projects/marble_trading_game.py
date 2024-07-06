# Import the modules
import random
from random import randrange
attempt = 0
# User start the game with 1000 $
money = 1000
# Define the bag with 10 marbles (6 green and 4 red)
marbles_bag = ['red', 'green', 'red', 'green', 'red', 'green', 'red', 'green', 'red', 'red']
# User will have variable number of draws
user_draws = random.randrange(1, 5 + 1)

for draws in range(user_draws):
# If user lose half of his money game is over
    if money >= 501:  

# Before each draw user define how much he will bet
        user_bet = int(input(f'How much you whant to bet?: '))
# User draw a random marble from the bag
        random_marble = random.choice(marbles_bag)    
# If user draw a green win the same ammount, if he draw a red he lose the amount he bet
        if random_marble == 'green':
            marbles_bag.remove('green')
            money += user_bet
# Print out data as user go along
            print(f'You take a {random_marble} one, you win :) you have {money}')
        elif random_marble == 'red':
            marbles_bag.remove('red')
            money -= user_bet
            print(f'You take a {random_marble} one, you lose :( you have {money}')
    else:        
        print(f"You loose half of your money :( you can't keep betting")
        break
# Marbles are replaced into bag after each round

# Bonus: replace two marbles 1 green with a black (10X winner) and 1 red (5X loser)
