import numpy as np

def forms_same_lattice(basis1, basis2):
    """
    Check if two bases form the same lattice.
    """
    return np.linalg.det(basis1) == np.linalg.det(basis2)

A = np.array([[1, 0], [0, 3]])
B = np.array([[1, 0], [0, 2]])

print(np.linalg.det(A), np.linalg.det(B))

