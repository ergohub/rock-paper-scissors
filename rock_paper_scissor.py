'''
Rock Paper scissors game
def play_game():
    user input choice r / p / s
    computer makes choice from r / p / s
    
    if player and computer have same answer:
        return "Its a tie!"

    if is_win(player, computer):
        return 'Your win'
    return 'You lose'
        
is_win(player, computer):
    r > s / s > p / p > r
    hence: 
    if (player == 'r' and computer == 's) or, etc.
        return true

print(play_game())
'''

import random

def play():
    user = input("1,2,3, Rock (R), Paper (P), Scissors (S): ").lower()
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'It\'s a draw'

    if is_win(user, computer):
        return 'You Win!!'
    return 'You Lose!!'

def is_win(player, computer):
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') \
    or (player == 'p' and computer == 'r'):
        return True

print(play())
