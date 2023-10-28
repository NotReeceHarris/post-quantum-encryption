import numpy as np

def generate_vector(num_of_dimentions=2, max_value=50):
    basis = np.random.randint(0, max_value, (num_of_dimentions))

    while basis[0] == basis[1] and (basis[0] == 0 and basis[1] == 0):
        basis = np.random.randint(0, max_value, (num_of_dimentions))

    return basis

def generate_basis(num_of_dimensions=2):
    basis = []

    while basis.__len__() < num_of_dimensions:
        vector = generate_vector(num_of_dimensions)
        if not any((vector == existing_vector).all() for existing_vector in basis):
            basis.append(vector)

    return basis

print(generate_basis(2))

print([
    generate_vector(2),
    list(generate_vector(2))
])