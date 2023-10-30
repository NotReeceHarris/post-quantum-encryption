import numpy as np
import math
import matplotlib.pyplot as plt
import random
import time

good_angle = 40
generated_bases = []

def generate_vector(num_of_dimentions=2, max_value=15):
    basis = np.random.randint(0, max_value, (num_of_dimentions))

    while basis[0] == basis[1] or (basis[0] == 0 and basis[1] == 0):
        basis = np.random.randint(0, max_value, (num_of_dimentions))

    return basis

def generate_basis(num_of_dimensions=2):
    basis = []

    while basis.__len__() != num_of_dimensions and basis not in generated_bases:
        while basis.__len__() < num_of_dimensions:
            vector = generate_vector(num_of_dimensions)
            if not any((vector == existing_vector).all() for existing_vector in basis):
                basis.append(vector)

    generated_bases.append(basis)
    return basis

def find_angles(basis):
    start_point = (0, 0)

    points = []
    angles = []
    checked = []

    for vector in basis:
        points.append((vector[0], vector[1]))

    for x in range(0, points.__len__()):
        for y in range(0, points.__len__()):
            if x != y and ((x, y) not in checked):
                point_a = points[x]
                point_b = points[y]
                vector_a = (point_a[0] - start_point[0], point_a[1] - start_point[1])
                vector_b = (point_b[0] - start_point[0], point_b[1] - start_point[1])
                dot_product = vector_a[0] * vector_b[0] + vector_a[1] * vector_b[1]
                magnitude_a = math.sqrt(vector_a[0]**2 + vector_a[1]**2)
                magnitude_b = math.sqrt(vector_b[0]**2 + vector_b[1]**2)
                angle_radians = math.acos(max(-1, min(1, dot_product / (magnitude_a * magnitude_b))))
                angle_degrees = math.degrees(angle_radians)

                if angle_degrees < good_angle:
                    return False

                checked.append((x, y))
                checked.append((y, x))
                angles.append(round(angle_degrees))

                print(angles)
    
    return angles

def is_bad_basis(basis):
    angles = find_angles(basis)

    for x in range(0, angles.__len__()):
        if angles[x] > 5:
            return False

    return True

def is_good_basis(basis):
    angles = find_angles(basis)

    if angles == False:
        return False
    
    for x in range(0, angles.__len__()):
        if angles[x] < good_angle:
            return False

    return True

def bruteforce_good_basis(dimensions):
    basis = generate_basis(dimensions)

    while not is_good_basis(basis):
        basis = generate_basis(dimensions)

    return basis

if __name__ == "__main__":
    dimensions = 4

    start = time.time()
    good_basis = bruteforce_good_basis(dimensions)
    end = time.time()

    print(good_basis, find_angles(good_basis), end - start)