import random
from player import Player
from gestures import list_of_gestures
list_of_names = ['Bender', 'Joey', 'Roger', 'Brian', 'Bobby', 'Jacob']


class AI_bot(Player):
    def __init__(self):
        self.name = random.choice(list_of_names)
        self.gesture = ''
        self.win_counter = 0
        self.select_gesture ()


    def select_gesture(self):
        self.gesture = random.choice(list_of_gestures)


