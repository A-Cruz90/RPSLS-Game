from gestures import list_of_gestures


class Player:
    def __init__(self, name):
        self.name = name 
        self.gesture = ""
        self.select_gesture()


    def select_gesture(self):
        print("0 For Rock")
        print("1 for Paper")
        print("2 for Scissors")
        print("3 for Lizard")
        print("4 for Spock")
        print('Please select a number beween 0 and 4' )
        self.gesture = input()

