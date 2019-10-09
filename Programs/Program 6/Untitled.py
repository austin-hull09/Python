import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

buildings = pd.read_csv('buildings.csv')
buildings = pd.DataFrame(buildings)

print(buildings)


occurrences = []

for i in range(len(buildings)):
    occurrences.append(buildings.ix[i, "Year Built"])

frequency = []
for i in range(1896, 2018):
    frequency.append(occurrences.count(i))
    
buildings.plot(x="Year Built", y =frequency, kind='line', xticks=(range(1896, 2018)))
plt.show()

##
##print(frequency)
##    
##frequency.plt.plot(color='yellow')
##plt.xlabel("Student")
##plt.ylabel("Points Earned")
##plt.title("Joy and Beauty of Data Dashboard")
##plt.show()

##plt.figure("Buildings")
##plt.xlabel("Year")
##plt.ylabel("Number Built")
##plt.title("Buildings vs Year")
##plt.plot(buildings)
##plt.show()
