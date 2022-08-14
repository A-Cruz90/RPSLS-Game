import random
from player import Player
from gestures import list_of_gestures

print(list_of_gestures)

print("Please choose a gesture using numbers 0 - 4. Where 0 is Rock and so forth")

player.gesture = input()

if player.gesturue in list_of_gestures:
    ai.gesture = random.choice(list_of_gestures)
    print("You chose '{player.gesture}', the AI chose '{ai.gesture}'")

else:
    print("You chose an invalid choice. Please choose from the list provided. ")
        


