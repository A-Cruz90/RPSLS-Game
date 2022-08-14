from random import random
from gestures import Scissors, Spock, Rock, Paper, Lizard
from gestures import list_of_gestures
from player import Player
from ai import AI_bot

player_one = Player("Joey")
player_two = Player("Billy")
ai_bot = AI_bot()

def run_game():
    while run_game == True:
        print(list_of_gestures)
        player_one.gesture = input(" please select your gesture: ")
        player_two.gesture = input(" Please select your gesture: ")
        ai_bot.getsure = random.choice(list_of_gestures)

        if player_one.gesture == player_two.gesture :
            print(f"Both players chose {player_one.gesture}. Therefore it's a tie! ")
        elif player_one.gesture > player_two.gesture:
            player_one.win_counter += 1 
        elif player_two.gesture > player_one.gesture:
            player_two.win_counter += 1 
        elif player_one.win_counter or player_two.win_counter == 2:
            run_game = False

