from hands import list_of_gestures


class Player():
    def __init__(self, name):
        self.name = name 
        self.select_gesture()


    def select_gesture(self):
        print(f'{print(list_of_gestures)}Where as Rock is number 0 and so on ')
        print(f'Please select a number beween 0 nad 4' )
        input("# ")
        