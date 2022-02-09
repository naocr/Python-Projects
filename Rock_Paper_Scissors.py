# ROCK PAPER SCISSORS
# The clasic game
import random

def play():
    user = input("Pick one. 'r' for rock, 'p' for paper, 's' for scissors. Your choice: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return 'You won :)'

    return 'You lost :('

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())        