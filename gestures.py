from hands import Scissors, Spock, Rock, Paper, Lizard
from hands import list_of_gestures
from player import Player

player_one = Player("Billy")
player_two = Player("Johny")


def run_game ():
    run_game = True
    while run_game == True:
        win_counter = 0
        if Rock:
            run_game = False
            win_counter += 1 
        elif Paper:
            run_game = False
            win_counter += 1 
        elif Scissors:
            run_game = False
            win_counter += 1 
        elif Spock:
            run_game = False
            win_counter += 1 
        elif Lizard:
            run_game = False
            win_counter += 1 

