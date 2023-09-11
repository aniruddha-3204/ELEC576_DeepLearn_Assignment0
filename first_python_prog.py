# First Deep Learning Assignment
# This program returns the average of the numbers

def num_avg(values):
    result = 0
    for i in values:
        result += i
    return result / len(values)


list_numbers = [2.3, 8.0, 11.2, 5.9]
print('The average of the given numbers is:', num_avg(list_numbers))
