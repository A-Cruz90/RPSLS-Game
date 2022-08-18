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
        elif player_one.gesture == Rock and player_two.gesture == Scissors :
            print(f'{player_one.gesture} smashes {player_two.gesture}! ')
            player_one.win_counter += 1 
        elif player_one.gesture == Rock and player_two.gesture == Lizard :
            print(f'{player_one.gesture} crushes {player_two.gesture}! ')
            player_one.win_counter += 1
        elif player_one.gesture == Paper and player_two.getsure == Rock :
            print(f'{player_one.gesture} covers {player_two.gesture}! ')
            player_one.win_counter += 1
        elif player_one.gesture == Paper and player_two.gesture == Spock:
            print(f'{player_one.gesture} disproves {player_two.gesture}! ')
            player_one.win_counter += 1
        elif player_one.gesture == Scissors and player_two.gesture == Paper :
            print(f'{player_one.gesture} cuts {player_two.gesture}! ')
            player_one.win_counter += 1
        elif player_one.gesture == Scissors and player_two.gesture == Lizard :
            print(f'{player_one.gesture} dicapitates {player_two.gesture}! ')
            player_one.win_counter += 1
        elif player_one.gesture == Lizard and player_two.gesture == Spock :
            print(f'{player_one.gesture} poisons {player_two.gesture}! ')
            player_one.win_counter += 1
        elif player_one.gesture == Lizard and player_two.gesture == Paper :
            print(f'{player_one.gesture} eats {player_two.gesture}! ')
            player_one.win_counter += 1
        elif player_one.gesture == Spock and player_two.gesture == Scissors :
            print(f'{player_one.gesture} smashes {player_two.gesture}! ')
            player_one.win_counter += 1
        elif player_one.gesture == Spock and player_two.gesture == Rock :
            print(f'{player_one.gesture} vaporizes {player_two.gesture}! ')
            player_one.win_counter += 1


