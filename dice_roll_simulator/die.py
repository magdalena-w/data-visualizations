from random import randint

class Die():
    """Class representing a single dice"""

    def __init__(self, num_sides=6):
        """Assume that the dice are cube-shaped"""
        self.num_sides = num_sides

    def roll(self):
        """Returns a value between 1 and the num_sides a dice has."""
        return randint(1, self.num_sides)