import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------
# CSCI 127, Lab 12
# November 21, 2017
# Austin Hull
# -----------------------------------------------------

def read_file(name):
    input_file = open(name, "r")
    number_buckets = int(input_file.readline())
    total_counties = int(input_file.readline())

    county_populations = np.zeros([total_counties], dtype="int")
    for county_number in range(total_counties):
        line = input_file.readline().split(",")
        county_populations[county_number] = int(line[1])
    county_populations.sort()
    input_file.close()

    return number_buckets, county_populations

# -----------------------------------------------------

def print_summary(averages):
    print("Population Grouping Summary")
    print("---------------------------")
    for grouping in range(len(averages)):
        print("Grouping", grouping + 1, "has a population average of",
              averages[grouping])

# -----------------------------------------------------
# Do not change anything above this line
# -----------------------------------------------------

def calculate_averages(number_buckets, county_populations):
    n = int(len(county_populations) / number_buckets)
    array = np.zeros(4, dtype='int')
    position = 0
    for i in range(number_buckets):
        a = 0
        for i in range(n):
            a += county_populations[i]
        county_populations = county_populations[n:]
        avg = ("%.0f" % (a / n))
        array[position] = avg
        position += 1
    return(array)
# -----------------------------------------------------

def graph_summary(averages):
    plt.figure("CSCI 127, Lab 12")
    plt.title("Montana County Population Analysis")
    num = []
    for number in range(number_buckets+1):
        if number > 0:
            num.append(number)
    plt.plot(num, averages, "c--")
    plt.plot(num, averages, 'bh')
    plt.xlabel('County Groupings')
    plt.ylabel('County Population Average')
    plt.xticks(np.arange(1,5,1))
    plt.show()

# -----------------------------------------------------

number_buckets, county_populations = read_file("montana-counties.txt")
averages = calculate_averages(number_buckets, county_populations)
print_summary(averages)
graph_summary(averages)
