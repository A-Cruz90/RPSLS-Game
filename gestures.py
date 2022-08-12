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
            win_counter += 1 
            win_counter= 2
            run_game = False
        elif Paper:
            win_counter += 1 
            win_counter = 2
            run_game = False
        elif Scissors:
            win_counter += 1 
            win_counter = 2
            run_game = False
        elif Spock:
            win_counter += 1 
            win_counter = 2
            run_game = False
        elif Lizard:
            win_counter += 1 
            win_counter = 2
            run_game = False

