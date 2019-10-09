##-------------------------------------
##CSCI 127, Program 6
##Austin Hull, Peter Mitzel
##12/8/2017
##-------------------------------------


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


buildings = pd.read_csv('buildings.csv') #received data from external sheet
buildings = buildings.sort_values("Year Built")

def first_graph(): #graphing the number of buildings constructed each year
    plt.figure("Montana State Buildings") 
    buildings["Year Built"].value_counts(sort=False).plot(kind="bar", color="red")
    plt.xlabel("Year")
    plt.ylabel("Number of Buildings Built")
    plt.title("Buildings Constructed per Year")

def second_graph(): #graphing the square footage of buildings built each year
    plt.figure("Montana State Buildings")
    plt.title("Year Built vs Square Footage")
    buildings.plot(x="Year Built", y="Square Feet", kind="scatter", color="blue")
    plt.xlabel("Year Built")
    plt.ylabel("Square Feet")
    plt.show()

def main(): 
    first_graph()
    second_graph()

main()
