from random import random
from gestures import Scissors, Spock, Rock, Paper, Lizard
from gestures import list_of_gestures
from player import Player

player_one = Player("")
player_two = Player("")


def run_game():
    print("How many players? ")
    print(input("0, 1, 2?: "))
    while run_game == True:
        print(list_of_gestures)
        player_one.gesture = input(" please select your gesture: ")
        player_two.gesture = input(" Please select your gesture: ")
        ai_bot.getsure = random.choice(list_of_gestures)

        if player_one.gesture > player_two.gesture:
            player_one.win_counter += 1 
        elif player_two.gesture > player_one.gesture:
            player_two.win_counter += 1 
        elif player_one.gesture == player_two.gesture :
            print
        elif player_one.win_counter or player_two.win_counter == 2:
            run_game = False