from board import *
from solver import *

board1 = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1]
]

board2 = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

def test_board_str_to_matrix():
    string = "12356347"
    matrix = board_str_to_matrix(string)

    print(matrix)

def test_board_matrix_to_str():
    print(board_matrix_to_str(board1))

def test_random_chessboard():
    b = random_board()
    print(b)

def test_queen_locations():
    print(queen_locations(board1))

    b = random_board()
    print(b)

    print(queen_locations(b.board))

def test_number_of_conflicts():
    b = random_board()
    print(b)
    print(number_of_conflicts(b.board))
    print(number_of_conflicts(board2))

def test_conflict_matrix():
    b = Chessboard(board_matrix=board2)

    print(b)

    print(b.conflict_matrix())

def test_minimum_queens():
    b = Chessboard(board_matrix=board2)
    print(b)
    print(pretty_print_matrix(b.conflict_matrix()))
    print(b.minimum_queens())

def test_random_minimal_successor():
    b = Chessboard(board_matrix=board2)
    print(b)

    random_minimal_successor(b)
    print(b)

def test_random_minimal_successor_2():
    b = random_board()
    print("h =", b.conflicts())
    print(b)

    for _ in range(10):
        random_minimal_successor(b)
        print("h =", b.conflicts())
        print(b)

def test_hill_climbing_solver():
    b = random_board(n=8)
    print("h =", b.conflicts())
    print(b)

    solver = HillClimbingSolver(board=b, n=8)

    solution = solver.solve()
    print("h =", solution.conflicts())
    print(solution)

def test_random_successor():
    b = random_board()
    print("h =", b.conflicts())
    print(b)

    b.random_successor()
    print("h =", b.conflicts())
    print(b)

def test_temperature():
    t0 = 100
    for t in range(1000):
        temp = temperature(t, t0)
        print(temp)
        if temp <= 0.00001:
            print(t)
            break

def test_simulated_annealing_solver():
    b = random_board(n=8)
    print("h =", b.conflicts())
    print(b)

    solver = SimulatedAnnealingSolver(board=b, n=8)

    solution = solver.solve()
    print("h =", solution.conflicts())
    print(solution)


if __name__ == '__main__':
    # test_board_str_to_matrix()
    # test_board_matrix_to_str()
    # test_random_chessboard()
    # test_queen_locations()
    # test_number_of_conflicts()
    # test_conflict_matrix()
    # test_minimum_queens()
    # test_random_minimal_successor_2()
    # test_hill_climbing_solver()
    # test_random_successor()
    # test_temperature()
    test_simulated_annealing_solver()
