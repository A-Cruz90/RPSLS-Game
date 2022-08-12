list_of_gestures = ["Rock","Scissors","Spock","Lizard","Paper"]


class Scissors():
    def __init__(self):
        Scissors > Paper
        Scissors > Lizard


class Rock():
    def __init__(self):
        Rock > Scissors
        Rock > Lizard


class Paper():
    def __init__(self):
        Paper > Rock
        Paper > Spock


class Lizard():
    def __init__(self):
        Lizard > Paper
        Lizard > Spock


class Spock():
    def __init__(self):
        Spock > Scissors
        Spock > Rock
