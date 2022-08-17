from random import random
from gestures import Scissors, Spock, Rock, Paper, Lizard
from gestures import list_of_gestures
from player import Player


player_one = Player(input("Player one, what is your name: "))
player_two = Player(input("Player two, what is your name: "))


def run_game():
    while True:
        player_one.select_gesture()
        player_two.select_gesture()
        print(f'{player_one.name} threw {player_one.gesture}! ')
        print(f'{player_two.name} threw {player_two.gesture}! ')

        if player_one.gesture == player_two.gesture :
            print(f"Both players chose {player_one.gesture}. Therefore it's a tie! ")
        elif player_one.gesture > player_two.gesture:
            print(f'{player_one.gesture} beats {player_two.gesture}! ')
            player_one.win_counter += 1 
        elif player_two.gesture > player_one.gesture:
            print(f'{player_two.gesture} beats {player_one.gesture}! ')
            player_two.win_counter += 1 
        elif player_one.win_counter or player_two.win_counter == 2:
            break

