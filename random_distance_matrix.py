import numpy as np


def input_with_validation(input_string, condition_number):
    while True:
        try:
            input_number = int(input(input_string))
            if not input_number > int(condition_number):
                raise ValueError
            break
        except ValueError:
            print("Error: " + input_string[0:(len(input_string)-2)] + " is to be greater than " + str(condition_number))
    return input_number


locations_number = input_with_validation("Number of locations: ", 1)
lower_limit = input_with_validation("Lower draw limit: ", 0)
upper_limit = input_with_validation("Upper draw limit: ", lower_limit)

vertex_list = []
distance_matrix = np.random.randint(lower_limit, high=upper_limit, size=(locations_number, locations_number))
for i in range(locations_number):
    distance_matrix[i][i] = 0
    vertex_list.append(i)
vertex_list.remove(0)
print(distance_matrix)
