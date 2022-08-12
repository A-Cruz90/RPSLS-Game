from hands import Scissors, Spock, Rock, Paper, Lizard
from hands import list_of_gestures
from player import Player

player_one = Player("Billy")
player_two = Player("Johny")


def run_game ():
    run_game = True
    player_one.win_counter = 0
    player_two.win_counter = 0 
    while run_game == True:
        if player_one.gesture > player_two.gesture:
            player_one.win_counter += 1 
        elif player_two.gesture > player_one.gesture:
            player_two.win_counter += 1 
        elif player_one.gesture == player_two.gesture :
            print
        elif player_one.win_counter or player_two.win_counter == 2:
            run_game = False