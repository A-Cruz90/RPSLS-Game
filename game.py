from random import random
from gestures import Scissors, Spock, Rock, Paper, Lizard
from gestures import list_of_gestures
from player import Player
from human import Human
from ai import AI_bot

class Game():
    def __init__(self):
        super().__init__
        self.player_one = ''
        self.player_two = ''
       
    def choose_player(self):
        user_input = input("How many players? ")
        if user_input == '1':
            self.player_one = Human(input('Player, What is your name?: '))
            self.player_two = AI_bot()
        elif user_input == '2':
            self.player_one = Human(input('Player, What is your name?: '))
            self.player_two = Human(input('Player, What is your name?: '))



    def run_game(self):
        while True:
            self.player_one.select_gesture()
            self.player_two.select_gesture()
            print(f'{self.player_one.name} threw {self.player_one.gesture}! ')
            print(f'{self.player_two.name} threw {self.player_two.gesture}! ')

            if self.player_one.gesture == self.player_two.gesture :
                print(f"Both players chose {self.player_one.gesture}. Therefore it's a tie! ")
            elif self.player_one.gesture == 'Rock' and self.player_two.gesture == 'Scissors' :
                print(f'{self.player_one.gesture} smashes {self.player_two.gesture}! ')
                print(f'{self.player_one.name} WINS!!!')
                self.player_one.win_counter += 1 
            elif self.player_one.gesture == 'Rock' and self.player_two.gesture == 'Lizard' :
                print(f'{self.player_one.gesture} crushes {self.player_two.gesture}! ')
                print(f'{self.player_one.name} WINS!!!')
                self.player_one.win_counter += 1
            elif self.player_one.gesture == 'Paper' and self.player_two.getsure == 'Rock' :
                print(f'{self.player_one.gesture} covers {self.player_two.gesture}! ')
                print(f'{self.player_one.name} WINS!!!')
                self.player_one.win_counter += 1
            elif self.player_one.gesture == 'Paper' and self.player_two.gesture == 'Spock':
                print(f'{self.player_one.gesture} disproves {self.player_two.gesture}! ')
                print(f'{self.player_one.name} WINS!!!')
                self.player_one.win_counter += 1
            elif self.player_one.gesture == 'Scissors' and self.player_two.gesture == 'Paper' :
                print(f'{self.player_one.gesture} cuts {self.player_two.gesture}! ')
                print(f'{self.player_one.name} WINS!!!')
                self.player_one.win_counter += 1
            elif self.player_one.gesture == 'Scissors' and self.player_two.gesture == 'Lizard' :
                print(f'{self.player_one.gesture} dicapitates {self.player_two.gesture}! ')
                print(f'{self.player_one.name} WINS!!!')
                self.player_one.win_counter += 1
            elif self.player_one.gesture == 'Lizard' and self.player_two.gesture == 'Spock' :
                print(f'{self.player_one.gesture} poisons {self.player_two.gesture}! ')
                print(f'{self.player_one.name} WINS!!!')
                self.player_one.win_counter += 1
            elif self.player_one.gesture == 'Lizard' and self.player_two.gesture == 'Paper' :
                print(f'{self.player_one.gesture} eats {self.player_two.gesture}! ')
                print(f'{self.player_one.name} WINS!!!')
                self.player_one.win_counter += 1
            elif self.player_one.gesture == 'Spock' and self.player_two.gesture == 'Scissors' :
                print(f'{self.player_one.gesture} smashes {self.player_two.gesture}! ')
                print(f'{self.player_one.name} WINS!!!')
                self.player_one.win_counter += 1
            elif self.player_one.gesture == 'Spock' and self.player_two.gesture == 'Rock' :
                print(f'{self.player_one.gesture} vaporizes {self.player_two.gesture}! ')
                print(f'{self.player_one.name} WINS!!!')
                self.player_one.win_counter += 1

            elif self.player_two.gesture == 'Rock' and self.player_one.gesture == 'Scissors' :
                print(f'{self.player_two.gesture} smashes {self.player_one.gesture}! ')
                print(f'{self.player_two.name} WINS!!!')
                self.player_two.win_counter += 1 
            elif self.player_two.gesture == 'Rock' and self.player_one.gesture == 'Lizard' :
                print(f'{self.player_two.gesture} crushes {self.player_one.gesture}! ')
                print(f'{self.player_two.name} WINS!!!')
                self.player_two.win_counter += 1
            elif self.player_two.gesture == 'Paper' and self.player_one.getsure == 'Rock' :
                print(f'{self.player_two.gesture} covers {self.player_one.gesture}! ')
                print(f'{self.player_two.name} WINS!!!')
                self.player_two.win_counter += 1
            elif self.player_two.gesture == 'Paper' and self.player_one.gesture == 'Spock':
                print(f'{self.player_two.gesture} disproves {self.player_one.gesture}! ')
                print(f'{self.player_two.name} WINS!!!')
                self.player_two.win_counter += 1
            elif self.player_two.gesture == 'Scissors' and self.player_one.gesture == 'Paper' :
                print(f'{self.player_two.gesture} cuts {self.player_one.gesture}! ')
                print(f'{self.player_two.name} WINS!!!')
                self.player_two.win_counter += 1
            elif self.player_two.gesture == 'Scissors' and self.player_one.gesture == 'Lizard' :
                print(f'{self.player_two.gesture} dicapitates {self.player_one.gesture}! ')
                print(f'{self.player_two.name} WINS!!!')
                self.player_two.win_counter += 1
            elif self.player_two.gesture == 'Lizard' and self.player_one.gesture == 'Spock' :
                print(f'{self.player_two.gesture} poisons {self.player_one.gesture}! ')
                print(f'{self.player_two.name} WINS!!!')
                self.player_two.win_counter += 1
            elif self.player_two.gesture == 'Lizard' and self.player_one.gesture == 'Paper' :
                print(f'{self.player_two.gesture} eats {self.player_one.gesture}! ')
                print(f'{self.player_two.name} WINS!!!')
                self.player_two.win_counter += 1
            elif self.player_two.gesture == 'Spock' and self.player_one.gesture == 'Scissors' :
                print(f'{self.player_two.gesture} smashes {self.player_one.gesture}! ')
                print(f'{self.player_two.name} WINS!!!')
                self.player_two.win_counter += 1
            elif self.player_two.gesture == 'Spock' and self.player_one.gesture == 'Rock' :
                print(f'{self.player_two.gesture} vaporizes {self.player_one.gesture}! ')
                print(f'{self.player_two.name} WINS!!!')
                self.player_two.win_counter += 1


