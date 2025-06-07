def get_user_board():
    board = []
    print("Enter 9 rows of 9 digits (use 0 for empty spaces):")
    for i in range(9):
        while True:
            row_input = input(f"Row {i + 1}: ")
            if len(row_input) == 9 and row_input.isdigit():
                board.append([int(char) for char in row_input])
                break
            else:
                print("Invalid input. Please enter exactly 9 digits (0–9).")
    return board

board = get_user_board()

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    box_x = (col // 3) * 3
    box_y = (row // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[box_y + i][box_x + j] == num:
                return False
    return True


def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()

print("Initial board:")
print_board(board)
solve(board)
print("\nSolved board:")
print_board(board)
