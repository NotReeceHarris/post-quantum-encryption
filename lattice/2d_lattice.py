import numpy as np
import math
import matplotlib.pyplot as plt
import random
import time

good_angle = 50

def generate_vector(max_value=15):
    basis = np.random.randint(0, max_value, (2))

    while basis[0] == basis[1] or (basis[0] == 0 and basis[1] == 0):
        basis = np.random.randint(0, max_value, (2))

    return basis

def generate_basis():
    basis = []

    while basis.__len__() < 2:
        vector = generate_vector()
        if not any((vector == existing_vector).all() for existing_vector in basis):
            basis.append(vector)

    return [list(basis[0]), list(basis[1])]

def find_angle(basis):
    start_point = (0, 0)
    point_a = [basis[0][0], basis[0][1]]
    point_b = [basis[1][0], basis[1][1]]
    vector_a = (point_a[0] - start_point[0], point_a[1] - start_point[1])
    vector_b = (point_b[0] - start_point[0], point_b[1] - start_point[1])
    dot_product = vector_a[0] * vector_b[0] + vector_a[1] * vector_b[1]
    magnitude_a = math.sqrt(vector_a[0]**2 + vector_a[1]**2)
    magnitude_b = math.sqrt(vector_b[0]**2 + vector_b[1]**2)
    angle_radians = math.acos(max(-1, min(1, dot_product / (magnitude_a * magnitude_b))))
    angle_degrees = math.degrees(angle_radians)

    return angle_degrees

def is_bad_basis(basis):
    angles = find_angle(basis)

    for x in range(0, angles.__len__()):
        if angles[x] > 5:
            return False

    return True

def is_good_basis(basis):
    angles = find_angle(basis)

    if angles < good_angle:
        return False

    return True

def generate_good_basis():
    basis = generate_basis()

    while not is_good_basis(basis):
        basis = generate_basis()

    return basis

def generate_bad_basis(good_basis):

    points = [
        [good_basis[0][0], good_basis[0][1]],
        [good_basis[1][0], good_basis[1][1]]
    ]

    vector_a = [good_basis[0][0], good_basis[0][1]]
    vector_b = [good_basis[1][0], good_basis[1][1]]

    for x in range(0, 8000):
        direction = random.randint(0, 1)
        negative = random.randint(0, 2) == 0

        if negative:
            vector_a[0] -= points[direction][0]
            vector_a[1] -= points[direction][1]
        else:
            vector_a[0] += points[direction][0]
            vector_a[1] += points[direction][1]

        direction = random.randint(0, 1)
        negative = random.randint(0, 3) == 1

        if negative:
            vector_b[0] -= points[direction][0]
            vector_b[1] -= points[direction][1]
        else:
            vector_b[0] += points[direction][0]
            vector_b[1] += points[direction][1]

    return [vector_a, vector_b]


if __name__ == "__main__":
    start = time.time()
    good_basis = generate_good_basis()
    end = time.time()

    print(good_basis, find_angle(good_basis), end-start)

    start = time.time()
    bad_basis = generate_bad_basis(good_basis)
    end = time.time()

    print(bad_basis, find_angle(bad_basis), end-start)