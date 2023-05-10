# Original author: https://gist.github.com/jpwhite3/43037f283cb8b097ec7d19e33ac8006e

import random

CHOICES = 'rps'


def get_player_choice():
    """Get user input and validate it is one of the choices above"""
    player_choice = None
    while player_choice is None:
        player_choice = input('Choices: \n(R)ock \n(P)aper \n(S)cissors \n\nPick: ')
        if player_choice.lower() not in CHOICES:
            player_choice = None
    return player_choice.lower()


def get_computer_choice():
    """Have the computer pick one of the valid choices at random"""
    computer_choice = random.randint(0, 2)
    computer_choice = CHOICES[computer_choice]
    return computer_choice


def is_draw(player_choice, computer_choice):
    """Check if game was a draw"""
    if player_choice == computer_choice:
        return True


def print_winner(player_choice, computer_choice):
    """Check to see who won"""
    if player_choice == 'r' and computer_choice == 's':
        print('Player wins!')
    elif player_choice == 's' and computer_choice == 'p':
        print('Player wins!')
    elif player_choice == 'p' and computer_choice == 'r':
        print('Player wins!')
    else:
        print('Computer wins!')
        print(f'{computer_choice} beats {player_choice}')


def play_game():
    """play the game"""
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    if is_draw(player_choice, computer_choice):
        print(f"It's a draw, both players picked {player_choice}")
    else:
        print(f"Computer picked: {computer_choice}")
        print(f"Player picked: {player_choice}")
        print_winner(player_choice, computer_choice)


if __name__ == "__main__":
    play_game()
