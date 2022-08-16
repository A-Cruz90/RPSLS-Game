list_of_gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

rock = 0
paper = 1
scissors = 2
lizard = 3
spock = 4



class Scissors:
    def __init__(self):
        Scissors > Paper
        Scissors > Lizard


class Rock:
    def __init__(self):
        Rock > Scissors
        Rock > Lizard


class Paper:
    def __init__(self):
        Paper > Rock
        Paper > Spock


class Lizard:
    def __init__(self):
        Lizard > Paper
        Lizard > Spock


class Spock:
    def __init__(self):
        Spock > Scissors
        Spock > Rock
