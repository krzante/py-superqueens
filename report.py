from board import *
from solver import *

def random_test_solver(Solver=HillClimbingSolver, n=8, size=100):
    """Tests how many solutions are successful with greedy hill climbing."""
    successful = 0

    for _ in range(size):
        board = random_board(n)
        solver = Solver(board, n)

        solved = solver.solve()

        if solved.conflicts() == 0:
            successful += 1

    return successful, size

def generate_test_cases(n=8, size=10, filepath="output/test.txt"):
    """Generates a list of test cases and outputs them to a file."""

    cases = []

    for _ in range(size):
        board = random_board(n)
        cases.append(board.as_string())

    with open(filepath, 'w') as f:
        for case in cases:
            f.write(case)
            f.write('\n\n')

if __name__ == '__main__':
    # generate_test_cases(n=8, size=10, filepath="test/cases.txt")

    successful, size = random_test_solver(HillClimbingSolver, n=8, size=500)
    percent = (successful / size) * 100

    print("Hill Climbing results: {0} successful out of {1} ({2:.2f}%)"
          .format(successful, size, percent))

    successful, size = random_test_solver(SimulatedAnnealingSolver, n=8,
                                          size=500)
    percent = (successful / size) * 100

    print("Simulated Annealing results: {0} successful out of {1} ({2:.2f}%)"
          .format(successful, size, percent))
