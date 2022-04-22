import numpy as np
import pandas as pd


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

distance_matrix = np.random.randint(lower_limit, high=upper_limit, size=(locations_number, locations_number))
vertex_list = []
for i in range(locations_number):
    distance_matrix[i][i] = 0
    vertex_list.append("m" + str(i))
print(distance_matrix)
df = pd.DataFrame(distance_matrix, index=vertex_list, columns=vertex_list)
# np.savetxt('distance_matrix.csv', distance_matrix, delimiter=',')
df.to_csv('distance_matrix.csv', index=True, header=True, sep=' ')
