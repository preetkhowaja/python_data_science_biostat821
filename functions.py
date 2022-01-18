### BIOSTAT 821: Homework 1
### Group: Himanshu Raj Bhantana and Preet Khowaja

# this function accepts a txt file and returns a list of lists of integers from that file

import math


def get_data(file):
    with open(file) as f:
        LL = []
        for line in f:
            list1 = line.split()
            list2 = []
            for i in range(0, len(list1)):
                list2.append(int(list1[i]))
            LL.append(list2)
        return LL


def analyze_data(list_of_lists, method):
    list_of_means = []
    for list in list_of_lists:
        mean1 = sum(list) / len(list)
        list_of_means.append(mean1)
    Average = sum(list_of_means) / len(list_of_means)

    if method == "average":
        return round(Average, 1)
    elif method == "standard deviation":
        pass


analyze_data(get_data("example.txt"), "average")
