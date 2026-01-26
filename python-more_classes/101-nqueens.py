#!/usr/bin/python3
"""N Queens problem solver"""
import sys


def is_safe(board, row, col, n):
    """Check if placing a queen at board[row][col] is safe

    Args:
        board: The current board state
        row: Row to check
        col: Column to check
        n: Size of the board

    Returns:
        bool: True if safe, False otherwise
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on left side
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    
    return True


def solve_nqueens_util(board, col, n, solutions):
    """Utility function to solve N Queens problem using backtracking

    Args:
        board: The current board state
        col: Current column
        n: Size of the board
        solutions: List to store all solutions
    """
    # Base case: If all queens are placed
    if col >= n:
        # Store the current solution
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    # Consider this column and try placing queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place queen
            board[i][col] = 1

            # Recur to place rest of the queens
            solve_nqueens_util(board, col + 1, n, solutions)

            # Backtrack: remove queen
            board[i][col] = 0


def solve_nqueens(n):
    """Solve the N Queens problem and print all solutions

    Args:
        n: Size of the board
    """
    # Initialize board with zeros
    board = [[0 for _ in range(n)] for _ in range(n)]

    # List to store all solutions
    solutions = []

    # Start solving from first column
    solve_nqueens_util(board, 0, n, solutions)

    # Print all solutions
    for solution in solutions:
        print(solution)


def main():
    """Main function to handle command line arguments"""
    # Check number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get N from arguments
    n_str = sys.argv[1]

    # Check if N is an integer
    try:
        n = int(n_str)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve N Queens problem
    solve_nqueens(n)


if __name__ == "__main__":
    main()
