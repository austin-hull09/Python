import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


buildings = pd.read_csv('buildings.csv') #received data from external sheet
buildings = buildings.sort_values("Year Built")


plt.figure("Montana State Buildings") #plot both sets of data
buildings["Year Built"].value_counts(sort=False).plot(kind="bar", color="red")
plt.xlabel("Year")
plt.ylabel("Number of Buildings Built")
plt.title("Buildings Constructed per Year")
plt.show()

#Mine plots correctly besides showing 1896, 1909 and 1910 on the right end of the 
#graph for some reason
