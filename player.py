import gestures
import random


class Player:
    def __init__(self,name):
        self.name = "" 
        self.gesture = ""
        self.select_gesture()
        self.win_counter = 0


    def select_gesture(self): 
        print("Your choices are as follow: ")
        print("0 For Rock")
        print("1 for Paper")
        print("2 for Scissors")
        print("3 for Lizard")
        print("4 for Spock")

        

