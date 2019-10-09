# -----------------------------------------------------
# CSCI 127, Lab 13
# November 28, 2017
# Austin Hull
# -----------------------------------------------------



import random
import matplotlib.pyplot as plt
import numpy as np

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
points = []

for i in range(10000):
    point_value = 0
    for i in range(2):
        card = random.choice(cards)
        if card == 'Jack' or card == 'Queen' or card == 'King':
            point_value += 10
        elif card == 'Ace':
            if point_value < 11:
                point_value += 11
            else:
                point_value += 1
        else:
            point_value += int(card)
    points.append(point_value)
    
plt.figure("CSCI 127, Lab 13")
plt.hist(points, bins=np.arange(4, 23), facecolor = 'g', align = 'left', density = True)
plt.title("Histogram of BlackJack Hands")
plt.xlabel("Hand Value")
plt.ylabel("Probability")
plt.xticks(np.arange(4, 22))
plt.grid(True)
plt.show()
