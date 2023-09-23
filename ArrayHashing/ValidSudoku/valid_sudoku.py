
from collections import defaultdict

# https://leetcode.com/problems/valid-sudoku/S


"""
1. Create sets for rows, cols, and squares

2. loop over rows:
    loop over cols:
        - Check if piece is empty, skip if so
        - Check if current piece is already in rows and cols sets
        - To check square, Integer divide row and col by 3
                If already present: return False

        Otherwise: Add piece to rows, cols, and squares sets

3. Return True

"""


def is_valid_sudoku(board):
    # Time O(9^2)
    # Space: O(9^2)
    cols = defaultdict(set)  # key = col num, val = set of values
    rows = defaultdict(set)
    squares = defaultdict(set)  # key = (r / 3, c /3)

    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                continue
            if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                return False

            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])

    return True


#     public boolean isValidSudoku(char[][] board) {
#     Set seen = new HashSet();
#     for (int i=0; i<9; ++i) {
#         for (int j=0; j<9; ++j) {
#             char number = board[i][j];
#             if (number != '.')
#                 if (!seen.add(number + " in row " + i) ||
#                     !seen.add(number + " in column " + j) ||
#                     !seen.add(number + " in block " + i/3 + "-" + j/3))
#                     return false;
#         }
#     }
#     return true;
# }


def valid_soduku_with_strings(board):
    seen = set()

    for r in range(9):
        for c in range(9):
            number = board[r][c]
            if number == '.':
                continue
            else:
                if ((f'{number} in row {r}') in seen or
                   (f'{number} in col {c}') in seen or
                   (f'{number} in square {r//3, c//3}') in seen):
                    return False

                else:
                    seen.add(f'{number} in row {r}')
                    seen.add(f'{number} in col {c}')
                    seen.add(f'{number} in square {r//3, c//3}')
    print(seen)
    return True


if __name__ == '__main__':
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]

    board2 = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]

    print(is_valid_sudoku(board))  # True
    print(is_valid_sudoku(board2))  # False

    # print(valid_soduku_with_strings(board))
    # print(valid_soduku_with_strings(board2))
