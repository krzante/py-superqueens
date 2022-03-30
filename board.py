"""board.py -- implements methods and classes to represent a chessboard and
heuristic/entropy measurements
"""
import random
from copy import deepcopy

def board_str_to_matrix(string):
    """Returns a matrix representation of a string of n characters, each of
    which representing the position of the ith queen in the jth row"""
    n = len(string)
    matrix = [[0 for j in range(n)] for i in range(n)]

    for j, c in enumerate(string):
        i = int(c)
        matrix[i][j] = 1

    return matrix

def board_matrix_to_str(matrix):
    """Returns the string representation of an n x n board where each of the
    characters of the string represents the ith position of the queen in the
    jth column"""
    string = ""
    n = len(matrix)

    for j in range(n):
        i = 0
        while i < n and matrix[i][j] != 1:
            i += 1

        string += str(i)

    return string

def random_board(n=8):
    """Returns a random n-queen chessboard.

    Args:
        n (int): The dimension of the n x n board.
    """
    matrix = [[0 for j in range(n)] for i in range(n)]

    for j in range(n):
        i = random.randint(0, n - 1)
        matrix[i][j] = 1

    return Chessboard(board_matrix=matrix)

def queen_locations(board):
    """Returns a list with the locations of the queens in a board.

    Args:
        board (list of list): the current board.
    """
    n = len(board)

    queens = []

    for j in range(n):
        for i in range(n):
            if board[i][j] == 1:
                queens.append((i, j))

    return queens

def is_attacking(i1, j1, i2, j2):
    """Returns True if the two queen locations are attacking each other.

    Args:
        i1, j1 (int): the coordinates of the first queen.
        i2, j2 (int): the coordinates of the second queen.
    """
    return (i1 == i2 or                   # Same row
            j1 == j2 or                   # Same column
            abs(i1 - i2) == abs(j1 - j2)) # Same diagonal

def number_of_conflicts(board):
    """Returns the number of queens attacking each other from a board.

    Args:
        board (list of list): the current board.
    """
    conflicts = 0
    queens = queen_locations(board)
    n = len(queens)

    for i in range(n):
        for j in range(i + 1, n):
            i1, j1 = queens[i]
            i2, j2 = queens[j]

            if is_attacking(i1, j1, i2, j2):
                conflicts += 1

    return conflicts

def pretty_print_matrix(matrix):
    """Returns a pretty print string of a n x n matrix of single digits or
    characters."""
    rows = []
    for r in matrix:
        s = " ".join(str(s) for s in r)
        rows.append(s)
    return "\n".join(rows)

def pretty_print_board(matrix):
    """Returns a pretty print representation of a board where the queen is
    represented as X"""
    rows = []
    for r in matrix:
        s = " ".join(("X" if s == 1 else "-") for s in r)
        rows.append(s)
    return "\n".join(rows)

class Chessboard:
    """Represents a n x n board with n queens.

    Args:
        n (int): The dimension of the n x n board.
    """
    def __init__(self, n=8, board_matrix=None):

        if board_matrix:
            self.board = board_matrix

        # Defines an empty board.
        else:
            # The matrix representation of the board.
            self.board = [[0 for j in range(n)] for i in range(n)]

            # Places queens in the first row of the board.
            for i in range(n):
                self.board[0][i] = 1

    def __repr__(self):
        return str(self.board)

    def __str__(self):
        """Returns the square representation of this board."""
        return pretty_print_board(self.board)

    def as_string(self):
        return pretty_print_matrix(self.board)

    def conflict_matrix(self):
        """Returns the matrix of conflicts of moving the queen from a column to
        a different row.
        """
        queens = queen_locations(self.board)
        n = len(queens)

        # Temporary matrix to find conflicts
        temp_matrix = deepcopy(self.board)

        # Conflict matrix
        conflicts = deepcopy(self.board)

        for i, j in queens:
            temp_matrix[i][j] = 0
            conflicts[i][j] = "X" # represents the queen location

            # Loop through the rows of the current queen column
            for k in range(n):
                if k != i:
                    temp_matrix[k][j] = 1

                    n_conflicts = number_of_conflicts(temp_matrix)
                    conflicts[k][j] = n_conflicts

                    temp_matrix[k][j] = 0

            temp_matrix[i][j] = 1

        return conflicts

    def move_queen(self, i1, j1, i2, j2):
        """Move queen from location (i1, j1) to (i2, j2)."""
        self.board[i1][j1] = 0
        self.board[i2][j2] = 1

    def conflicts(self):
        """Returns the number of conflicts of this board."""
        return number_of_conflicts(self.board)

    def minimum_queens(self):
        """Returns a list of queens that could be moved to the minimum conflict
        locations.

        Returns a list of pairs ((i1, j1), (i2, j2)), where the first
        parameter represents the queen location, and the second parameter
        represents a location that the queen could move to with lower number of
        conflicts.
        """
        queens = queen_locations(self.board)
        n = len(queens)

        conflicts = self.conflict_matrix()

        # List of minimum queens
        minima = []

        # Find the minimum value of conflicts
        minimum_conflict = float('inf')

        for i in range(n):
            for j in range(n):
                if (conflicts[i][j] != 'X' and
                    conflicts[i][j] < minimum_conflict):

                    minimum_conflict = conflicts[i][j]

        # Find the positions equal to the minimum
        for i, j in queens:
            for k in range(n):
                if conflicts[k][j] == minimum_conflict:
                    minima.append(((i, j), (k, j)))

        return minima

    def random_minimal_successor(self):
        """Updates the board with a random minimal successor.
        """
        possible_moves = self.minimum_queens()
        heuristic = self.conflicts()

        if heuristic != 0:
            queen, next_move = random.choice(possible_moves)
            i1, j1 = queen
            i2, j2 = next_move

            # print("h = {}, moving queen {} to {}".format(heuristic, queen,
                                                         # next_move))

            self.move_queen(i1, j1, i2, j2)

    def random_successor(self):
        """Updates the board at random.
        """
        n = len(self.board)

        # Pick a queen at random to move
        queens = queen_locations(self.board)
        i1, j1 = random.choice(queens)

        # Pick a random different row to move to
        i2 = i1
        while i2 == i1:
            i2 = random.randint(0, n-1)

        # print("moving queen {} to {}".format((i1, j1), (i2, j1)))

        self.move_queen(i1, j1, i2, j1)
