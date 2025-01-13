'''
This simple yet fun Python program lets you play the classic Rock, Paper, Scissors game against the computer. The game is interactive and follows these basic rules:

Rock beats Scissors
Scissors beats Paper
Paper beats Rock
'''
import random
from colorama import Fore, Back, Style

print("")
# Title of the Game
title = " Rock Paper Scissor Game ".upper()

# Grabs title and centers it. Then fills in 20 chars with =
print(title.center(50, "*"))
playerchoice = input(
    '''Enter the options listed below:

1. Rock
2. Paper
3. Scissors \n
Player Choice: ''').lower()

# Divider
print("".ljust(50, "*"))

cpuchoice = ['rock', 'paper', 'scissors']

final_choice = (random.choice(cpuchoice))

# output_choice = random(cpuchoice)
print(Fore.MAGENTA + f'''\nPlayer Choice: {playerchoice}''' + Fore.CYAN +
      f'''\nComputer choice: {final_choice}''')

# Player enters rock,paper, or scissors

if playerchoice == final_choice:
    print(Fore.YELLOW + '\nDraw! ')

elif playerchoice == 'rock' and final_choice != 'paper':
    print(Fore.GREEN + '\nYou Win!')

elif playerchoice == 'paper' and final_choice != 'scissors':
    print(Fore.GREEN + '\nYou Win! ')

elif playerchoice == 'scissor' and final_choice != 'rock':
    print(Fore.GREEN + '\nYou Win! ')

elif playerchoice not in cpuchoice:
    print(Fore.RED + '\n You entered an option that is not rock, paper, or scissors. Please try again later.')

else:
    print(Fore.RED + '\n You Lose!')
