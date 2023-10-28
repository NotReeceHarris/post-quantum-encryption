import random

class Lattice:
    """
    A lattice is a set of points in a space that are all a linear combination of
    a set of basis vectors. This class represents a lattice and can be used to
    generate points in the lattice.
    """

    def __init__(self, starting_point, basis_vectors):
        """
        Initialize a lattice object with a starting point and a set of basis
        vectors.
        """

        self.starting_point = starting_point
        self.basis_vectors = basis_vectors

    def calculate_moves(self, moves):
        """
        Calculate the coordinates of a point in the lattice given a list of moves.

        A move is an integer that represents the index of the basis
        vector to move along. A negative move represents moving in the opposite
        direction of the basis vector.
        """
        basis_vectors = self.basis_vectors
        coord = list(self.starting_point) 

        for move in moves:
            move_index = abs(move) - 1
            vector = [-x for x in basis_vectors[move_index]] if move < 0 else basis_vectors[move_index]
            coord = [c + v for c, v in zip(coord, vector)]

        return coord

def generate_random_moves(num_of_vectors, num_of_moves=10):
    """
    Generate a list of random moves.
    """
    moves = [random.randint(1, num_of_vectors) * random.choice([-1, 1]) for _ in range(num_of_moves)]
    return moves

def generate_random_basis_vectors(num_of_vectors=2, num_of_dimensions=2, max_value=10, min_value=0):
    """
    Generate a list of random basis vectors.
    """
    basis_vectors = [[random.randint(min_value, max_value) for _ in range(num_of_dimensions)] for _ in range(num_of_vectors)]
    return basis_vectors

def generate_random_starting_point(num_of_dimensions=2, max_value=10, min_value=0):
    """
    Generate a random starting point.
    """
    starting_point = [random.randint(min_value, max_value) for _ in range(num_of_dimensions)]
    return starting_point

def calculate_determinant(basis_vectors):
    """
    Calculate the determinant of a matrix formed by a set of basis vectors.

    The determinant of a matrix formed by a set of basis vectors is the volume
    of the parallelepiped formed by the basis vectors.
    """
    determinant = 0
    num_of_vectors = len(basis_vectors)
    num_of_dimensions = len(basis_vectors[0])

    if num_of_vectors == 1:
        determinant = basis_vectors[0][0]
    elif num_of_vectors == 2:
        determinant = basis_vectors[0][0] * basis_vectors[1][1] - basis_vectors[0][1] * basis_vectors[1][0]
    else:
        for i in range(num_of_vectors):
            minor = [[basis_vectors[j][k] for k in range(num_of_dimensions) if k != i] for j in range(1, num_of_vectors)]
            determinant += (-1) ** i * basis_vectors[0][i] * calculate_determinant(minor)

    return determinant

def is_linearly_independent(basis_vectors):
    """
    Check if a set of basis vectors are linearly independent.

    A set of basis vectors are linearly independent if the determinant of the
    matrix formed by the basis vectors is not zero.
    """
    determinant = calculate_determinant(basis_vectors)
    return determinant != 0

def generate_random_equivalent_bases(num_of_dimensions=2):
    """
    Generate 2 matching random lattices bases, one good and one bad.

    A good lattice is a lattice where the basis vectors are linearly independent. (perpendicular)
    A bad lattice is a lattice where the basis vectors are linearly dependent. (near parallel)

    Equivalent bases (i.e., bases that generate the same lattice) can be algebraically 
    characterized as follows. Two bases B,B'∈R^m*n are equivalent if and only if there exists 
    a unimodular matrix U∈Z^n*n (i.e., an integral matrix with determinant det(U)=±1) such that B'=BU.

    https://math.stackexchange.com/questions/4435793/check-if-two-bases-form-the-same-lattice

    """
    



if __name__ == '__main__':

    dimentions = 1
    vectors = 300

    min = -100
    max = 100

    print(generate_random_lattice())
    exit()

    starting_point = generate_random_starting_point(dimentions, max, min)
    basis_vecotors = generate_random_basis_vectors(vectors, dimentions, max, min)
    moves = generate_random_moves(vectors, 100)

    print('starting point: ', starting_point)
    # print('basis vectors: ', basis_vecotors)
    # print('moves: ', moves)

    lattice = Lattice(starting_point, basis_vecotors)
    point = lattice.calculate_moves(moves)

    print(point)