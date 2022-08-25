from player import Player

class Human(Player):
    def __init__(self,name):
        super().__init__()
        self.name = name
        self.favorite_gesture = ''
        self.favorite ()


        
    def favorite(self):
        favorite_gesture = print(input(f'What is your favorite gesture to throw down? '))
        self.favorite_gesture = favorite_gesture