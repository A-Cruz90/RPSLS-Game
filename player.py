import gestures
import random


class Player:
    def __init__(self):
        self.gesture = ''
        self.win_counter = 0
        self.list_of_getsures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

    def select_gesture(self): 
        print("Your choices are as follow: ")
        print("0 For Rock")
        print("1 for Paper")
        print("2 for Scissors")
        print("3 for Lizard")
        print("4 for Spock")

        user_input = input("Please select a number between 0 and 4. Where 0 = Rock and so on: ")
        if user_input == '0':
            self.gesture = self.list_of_getsures[0]        
        elif user_input == '1':
            self.getsure = self.list_of_getsures[1]            
        elif user_input == '2':
            self.gesture = self.list_of_getsures[2]            
        elif user_input == '3':
            self.gesture = self.list_of_getsures[3]    
        elif user_input == '4':
            self.gesture = self.list_of_getsures[4] 
        else:
            print(f'You have chosen a non valid option plesae try again!: ')
        



