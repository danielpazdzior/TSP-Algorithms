import numpy as np
from itertools import permutations
import sys


def path_print(path):
    path_string = "0 -> "
    for i in range(len(path)):
        path_string += str(path[i])
        path_string += " -> "
    path_string += "0"
    return path_string


def min_hamiltonian_path():
    all_permutations = list(permutations(vertex_list))
    min_hamiltonian_path_length = sys.maxsize
    min_hamiltonian_path_permutation = ()
    for permutation in all_permutations:
        hamiltonian_path = distance_matrix.item((permutation[0], 0)) + distance_matrix.item(
            (0, permutation[len(permutation) - 1]))
        for i in range(len(permutation) - 1):
            hamiltonian_path += distance_matrix.item((permutation[i + 1], permutation[i]))
        if hamiltonian_path < min_hamiltonian_path_length:
            min_hamiltonian_path_length = hamiltonian_path
            min_hamiltonian_path_permutation = permutation
    print("Tour: " + path_print(min_hamiltonian_path_permutation))
    print("Tour length: " + str(min_hamiltonian_path_length))
    return min_hamiltonian_path_permutation


n = 4
vertex_list = []
for i in range(n):
    vertex_list.append(i)
vertex_list.remove(0)
distance_matrix = np.matrix('0 2 9 10; 1 0 6 4; 15 7 0 8; 6 3 12 0')
min_hamiltonian_path()
