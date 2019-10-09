import numpy as np
import random

# -------------------------------------------------
# CSCI 127, Lab 11
# November 14, 2017
# Austin Hull
# -------------------------------------------------

class Die:

    def __init__(self, sides):
        """A constructor method to create a die"""
        self.sides = sides

    def roll(self):
        """A general method to roll the die"""
        return random.randint(1, self.sides)

# -------------------------------------------------

class Yahtzee:

    def __init__(self):
        """A constructor method that can record 5 dice rolls"""
        self.rolls = np.zeros(5, dtype=np.int16)

    def roll_dice(self):
        """A general method that rolls 5 dice"""
        for i in range(len(self.rolls)):
            self.rolls[i] = Die(6).roll()

    def count_outcomes(self):
        """A helper method that determines how many 1s, 2s, etc. were rolled"""
        counts = np.zeros(7, dtype=np.int16)
        for roll in self.rolls:
            counts[roll] += 1
        return counts

    def is_it_yahtzee(self):
        num = 0
        for i in range(len(self.rolls)):
            if self.rolls[i] == self.rolls[0]:
                num += 1
        if num == 5:
            return True

    def is_it_full_house(self):
        counts = self.count_outcomes()
        for count in counts:
            if 3 in counts:
                if 2 in counts:
                    return True

    def is_it_large_straight(self):
        counts = self.count_outcomes()
        num = 0
        if counts[1] == 0 or counts[6] == 0:
            for count in counts:
                if counts[count] == 1:
                    num += 1
        if num == 5:
            return True
# -------------------------------------------------
        
def main(how_many):
    
    yahtzees = 0
    full_houses = 0
    large_straights = 0
    game = Yahtzee()

    for i in range(how_many):
        game.roll_dice()
        if game.is_it_yahtzee():
            yahtzees += 1
        elif game.is_it_full_house():
            full_houses += 1
        elif game.is_it_large_straight():
            large_straights += 1
    
    print("Number of Rolls:", how_many)
    print("---------------------")
    print("Number of Yahtzees:", yahtzees)
    print("Yahtzee Percent:", "{:.2f}%\n".format(yahtzees * 100 / how_many))
    print("Number of Full Houses:", full_houses)
    print("Full House Percent:", "{:.2f}%\n".format(full_houses * 100 / how_many))
    print("Number of Large Straights:", large_straights)
    print("Large Straight Percent:", "{:.2f}%".format(large_straights * 100 / how_many))

# -------------------------------------------------

main(5000)
    
        
