from board import Chessboard, random_board
from solver import HillClimbingSolver, SimulatedAnnealingSolver
from copy import deepcopy

if __name__ == "__main__":
    print("CS 4200 Project 2")
    print("n-queens solver")

    n = 8

    while n != 0:
        print("----------------")
        print("Type in the dimension of the board, or 0 to exit:")
        n = int(input())
        print()

        if n == 0:
            continue

        b = random_board(n)

        print("Generated {}x{} board:".format(n, n))
        print(b)
        heuristic = b.conflicts()
        print("Number of conflicts =", heuristic, '\n')

        # Hill Climbing Solution
        hc = HillClimbingSolver(b, n)
        solution_hc = hc.solve()

        print("Hill Climbing Solution:")
        print(solution_hc)
        heuristic_hc = solution_hc.conflicts()
        print("Number of conflicts =", heuristic_hc)
        print("Successful: {}".format("YES" if heuristic_hc == 0 else "NO"))
        print()

        # Simulated Annealing
        hc = SimulatedAnnealingSolver(b, n)
        solution_hc = hc.solve()

        print("Simulated Annealing Solution:")
        print(solution_hc)
        heuristic_hc = solution_hc.conflicts()
        print("Number of conflicts =", heuristic_hc)
        print("Successful: {}".format("YES" if heuristic_hc == 0 else "NO"))

        print()
