import random

def is_valid(board, row, col, num):
    # Sprawdzanie, czy liczba może być umieszczona w danej komórce
    for c in range(9):
        if board[row][c] == num:
            return False
    for r in range(9):
        if board[r][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False
    return True

def _solve(board):
    # Rozwiązywanie Sudoku z losowym doborem liczb
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                numbers = list(range(1, 10))
                random.shuffle(numbers)  # losowa kolejność cyfr
                for num in numbers:
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if _solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def generate_full_sudoku():
    # Generowanie pełnej planszy Sudoku
    board = [[0] * 9 for _ in range(9)]
    _solve(board)
    return board

def generate_sudoku_with_empty_cells(empty_cells):
    # Generowanie Sudoku z określoną liczbą pustych komórek
    board = generate_full_sudoku()
    empty_positions = random.sample(range(81), empty_cells)
    
    for pos in empty_positions:
        row, col = pos // 9, pos % 9
        board[row][col] = 0  # Ustawienie na 0 (puste miejsce)
    
    return board

def format_sudoku(board):
    # Formatowanie planszy z 'x' zamiast '_'
    return '\n'.join([''.join([str(cell) if cell != 0 else 'x' for cell in row]) for row in board])

def save_sudoku_to_file(filename, board):
    # Zapisanie sformatujowanej planszy do pliku
    formatted_sudoku = format_sudoku(board)
    with open(filename, 'w') as f:
        f.write(formatted_sudoku)

# Przykład użycia
for i in range(1,21):
    empty_cells = 75
    filename = f"zad3_sudoku/empty_{empty_cells}/sudoku/sudoku_{i}.txt"

    board = generate_sudoku_with_empty_cells(empty_cells)
    save_sudoku_to_file(filename, board)
