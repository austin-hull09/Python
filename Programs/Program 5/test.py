import numpy as np

file = open('batting.txt', 'r')

li = file.readlines()

ar = np.zeros((int(li[0]), 5))


print(li)
print(ar)
