### BIOSTAT 821: Homework 1
### Group: Himanshu Raj Bhantana and Preet Khowaja

# this function accepts a txt file and returns a list of lists of integers from that file

def get_data(file):
    with open (file) as f:
        LL = []

        for line in f:
            list1 = line.split()
            list2=[]
            for i in range(0,len(list1)):
                list2.append(int(list1[i]))
            LL.append(list2)
        print(LL)


get_data('example.txt')


