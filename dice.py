import random

class Dice:
    @staticmethod
    def roll():
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        return total, (die1, die2)