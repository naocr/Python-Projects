# NUMBER GUESSER
import random
from secrets import choice

# COMPUTER
# The computer has a random number and you have to guess it
def guess(x):
    random_num = random.randint(1, x)
    guess = 0

    while guess != random_num:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_num:
            print('Sorry, number too low. Try again.')
        elif guess > random_num:
            print('Sorry, number too high. Try again.')

    print(f'You have guessed the number {random_num}. Congrats!')

# USER
# The user has a random number and the computer has to guess it
def computer_guess(x):
    guess = 0

    low = 1
    high = x
    response = ''

    while response != 'c':
        guess = random.randint(low, high)
        response = input(f'Is {guess} too high(h), too low(l) or correct(c)? ')
        if response == 'h':
            high = guess - 1
        elif response == 'l':
            low = guess + 1

    print(f'I have guessed the number {guess}. Yay!')
  
def pick():
    choice = input('Who do you want to guess? You(m) or the computer(c)?\n')
    max = int(input('What\'s the maximum of the range you want to guess?\n'))
    if choice == 'm':
        guess(max)
    else:
        computer_guess(max)    

pick()        
