from board import *
import random
from copy import deepcopy
from math import exp

class Solver:
    """A solver for the n-queens problem."""
    def __init__(self, board=None, n=8):
        if board is None:
            board = random_board(n)

        self.n = n
        self.board = deepcopy(board)

    def solve(self):
        raise NotImplementedError

class HillClimbingSolver(Solver):
    def solve(self):
        """Returns the solved hill climbing matrix."""
        return self.hill_climbing()

    def hill_climbing(self):
        """Returns the local minimum of the queen state."""
        current_board = deepcopy(self.board)

        while True:
            self.board.random_minimal_successor()

            # Local minimum reached
            if self.board.conflicts() >= current_board.conflicts():
                return current_board

            current_board = deepcopy(self.board)

# The exponent for the temperature function
ALPHA = 0.9

# The minimum temperature to consider
MIN_TEMPERATURE = 0.0001

# Maximum number of iterations in simulated annealing
MAX_ITERATIONS = 100000

def temperature(time, t0):
    """Temperature function (exponential decay) for the simulated annealing
    algorithm.

    Args:
        time (int): the current unit of time.
        t0 (float): the initial temperature.
    """
    return t0 * pow(ALPHA, time/20)

def accept_change(de, temp):
    """Returns True if we should accept the random suboptimal change in the
    simulated annealing algorithm.

    Args:
        de (int): The difference between the previous and current heuristic.
        temp (float): The current temperature.
    """
    prob = exp((-1 * abs(de)) / temp)
    # print(prob)
    return random.random() <= prob

class SimulatedAnnealingSolver(Solver):
    def solve(self):
        """Returns the solved hill climbing matrix or failure."""
        return self.simulated_annealing()

    def simulated_annealing(self):
        """Implements the simulated annealing algorithm to return a minimum of
        the queen state."""

        # Current time
        time = 1

        # The initial temperature
        t0 = 100

        while time < MAX_ITERATIONS:
            temp = temperature(time, t0)

            if self.board.conflicts() == 0:
                return self.board

            if temp <= MIN_TEMPERATURE:
                # print("iterations =",time)
                return self.board

            next_board = deepcopy(self.board)
            next_board.random_successor()

            de = next_board.conflicts() - self.board.conflicts()

            if de < 0 or accept_change(de, temp):
                self.board = next_board

            time += 1

        return self.board
