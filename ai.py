import random
from player import Player
from gestures import list_of_gestures

print(list_of_gestures)

print("Please choose a gesture using numbers 0 - 4. Where 0 is Rock and so on. ")

class AI_bot(Player):
    def __init__(self):
        self.gesture = random.choice(list_of_gestures)