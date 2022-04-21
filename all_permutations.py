import numpy as np


def path_print(path):
    path_string = "0 -> "
    for i in range(len(path)):
        path_string += str(path[i])
        path_string += " -> "
    path_string += "0"
    return path_string


def permutations(A):
    c = []
    for j in range(len(A)):
        c.append(0)

    min_hamiltonian_path_length = permutation_path(A)
    min_hamiltonian_path_permutation = A

    j = 0
    while j < len(A):
        if c[j] < j:
            if (j % 2) == 0:
                A[0], A[j] = A[j], A[0]
            else:
                A[c[j]], A[j] = A[j], A[c[j]]
            if permutation_path(A) < min_hamiltonian_path_length:
                min_hamiltonian_path_length = permutation_path(A)
                min_hamiltonian_path_permutation = A
            c[j] += 1
            j = 0
        else:
            c[j] = 0
            j += 1
    print("Tour: " + path_print(min_hamiltonian_path_permutation))
    print("Tour length: " + str(min_hamiltonian_path_length))


def permutation_path(permutation):
    hamiltonian_path = distance_matrix.item((permutation[0], 0)) + distance_matrix.item(
        (0, permutation[len(permutation) - 1]))
    for k in range(len(permutation) - 1):
        hamiltonian_path += distance_matrix.item((permutation[k + 1], permutation[k]))
    return hamiltonian_path


distance_matrix = np.loadtxt('distance_matrix.csv', delimiter=',')
n_rows, n_cols = distance_matrix.shape
if n_rows != n_cols:
    print("Matrix shape error (" + str(n_rows) + " rows, " + str(n_cols) + " columns)")
else:
    vertex_list = list(range(n_rows))
    vertex_list.remove(0)
    permutations(vertex_list)
