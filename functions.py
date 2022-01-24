### BIOSTAT 821: Homework 1
### Group: Himanshu Raj Bhantana and Preet Khowaja

# Importing math package in python
import math

# this function accepts a txt file and returns a list of lists of integers from that file
def get_data(file: str) -> list:
    with open(file) as f:
        LL = []
        for line in f:
            list1 = line.split()
            list2 = []
            for i in range(0, len(list1)):
                list2.append(int(list1[i]))
            LL.append(list2)
        return LL


## Helper function that computes average of all data
def average(list_of_lists: list) -> float:
    list_of_means = []
    for list in list_of_lists:
        mean1 = sum(list) / len(list)
        list_of_means.append(mean1)
    Average = sum(list_of_means) / len(list_of_means)
    return Average


## Helper function that computes standard deviation of all data
def sd(list_of_lists: list) -> float:
    Average = average(list_of_lists)
    sum_squared = 0
    lengths = 0
    for list in list_of_lists:
        for number in list:
            sum_squared += (number - Average) ** 2
        lengths += len(list)
    sd = math.sqrt(sum_squared / lengths)
    return sd


## Helper function that computes covariance of all data
def covariance(list_of_lists):
    list1 = list_of_lists[0]
    list2 = list_of_lists[1]
    mean1 = sum(list1) / len(list1)
    mean2 = sum(list2) / len(list2)
    subtracted1 = []
    subtracted2 = []
    for x in list1:
        subtracted1.append(x - mean1)
    for y in list2:
        subtracted2.append(y - mean2)
    sum_of_products = 0
    for i in range(len(subtracted1)):
        product = subtracted1[i] * subtracted2[i]
        sum_of_products += product
    return sum_of_products / len(list1)


## Helper function that computes correlation of all data
def corr(list_of_lists):
    list1 = list_of_lists[0]
    list2 = list_of_lists[1]
    mean1 = sum(list1) / len(list1)
    mean2 = sum(list2) / len(list2)
    sum_squared1 = 0
    sum_squared2 = 0
    for number in list1:
        sum_squared1 += (number - mean1) ** 2
    for number in list2:
        sum_squared2 += (number - mean2) ** 2
    sd_x = math.sqrt(sum_squared1 / len(list1))
    sd_y = math.sqrt(sum_squared2 / len(list2))
    cov = covariance(list_of_lists)
    corr = cov / (sd_x * sd_y)
    return corr


# This function computes various metrics from the input data
def analyze_data(list_of_lists: list, method: str) -> float:
    if method == "average":
        return round(average(list_of_lists), 1)
    elif method == "standard deviation":
        return round(sd(list_of_lists), 1)
    elif method == "covariance":
        return round(covariance(list_of_lists), 1)
    elif method == "correlation":
        return round(corr(list_of_lists), 3)
    raise ValueError(f"Unexpected input value {method}")


if __name__ == "__main__":
    print(analyze_data(get_data("example.txt"), "average"))
    print(analyze_data(get_data("example.txt"), "standard deviation"))
    print(analyze_data(get_data("example.txt"), "covariance"))
    print(analyze_data(get_data("example.txt"), "correlation"))
