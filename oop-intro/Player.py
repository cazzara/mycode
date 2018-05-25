from random import randint


class Player:
    def __init__(self, n):
        self.dice = []
        self.name = n

    def roll(self):
        self.dice = []
        for i in range(3):
            self.dice.append(randint(1, 6))

    def get_dice(self):
        return self.dice
 
    def get_name(self):
        return self.name
