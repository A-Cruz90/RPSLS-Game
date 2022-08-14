from gestures import list_of_gestures
import random


class Player:
    def __init__(self,name):
        list_of_gestures
        self.name = "" 
        self.gesture = ""
        self.select_gesture()


    def select_gesture(self):
        print("0 For Rock")
        print("1 for Paper")
        print("2 for Scissors")
        print("3 for Lizard")
        print("4 for Spock")
        print('Please select a number beween 0 and 4' )
        self.gesture = input("")
        if self.gesture in list_of_gestures:
            print(f'You chose {self.gesture}')

        else:
            print("You chose an invalid choice. Please choose from the list provided. ")
        

