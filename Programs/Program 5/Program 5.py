# -------------------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 5: World Series Batting Averages
# Peter Mitzel, Austin Hull
# Last Modified: 11/21/17
# -------------------------------------------------
# A brief description of the program
#--------------------------------------------------

import numpy as np

class Person:
    def __init__(self, first_name, last_name, in_file):
        self.first = first_name
        self.last = last_name
        self.in_file = open("batting.txt", 'r')

    def get_name(self):
        name = (self.first + self.last)

    def read_input(self):
        li = self.in_file.readlines()   #creates a list with each line from the input being an element of it
        ar = np.zeros((int(li[0]), 5))  #create an array that is 5 wide (for first, last, date, at bats, and hits) by the number of players tall

class Batter(Person):
    def __init__(self, first_name, last_name, position, at_bats, hits):
        self.first = first_name
        self.last = last_name
        self.position = position
        self.at_bats = at_bats
        self.hits = hits

class All_Batters:
    def __init__(self, batters):
        self.batters = batters
