def solver(pmd):
    def print_board(board):
        '''Prints the board'''
        pmd1 = []
        row1 = []
        row2 = []
        row3 = []
        row4 = []
        row5 = []
        row6 = []
        row7 = []
        row8 = []
        row9 = []
        for i in range(1, 10):
            for j in range(1, 10):
                if i == 1:
                    row1.append(board[i - 1][j - 1])
                if i == 2:
                    row2.append(board[i - 1][j - 1])
                if i == 3:
                    row3.append(board[i - 1][j - 1])
                if i == 4:
                    row4.append(board[i - 1][j - 1])
                if i == 5:
                    row5.append(board[i - 1][j - 1])
                if i == 6:
                    row6.append(board[i - 1][j - 1])
                if i == 7:
                    row7.append(board[i - 1][j - 1])
                if i == 8:
                    row8.append(board[i - 1][j - 1])
                if i == 9:
                    row9.append(board[i - 1][j - 1])

        pmd1 = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

        return pmd1

    def find_empty(board):
        '''Finds an empty cell and returns its position as a tuple'''

        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)

    def valid(board, pos, num):
        '''Whether a number is valid in that cell, returns a bool'''

        for i in range(9):
            if board[i][pos[1]] == num and (
                    i, pos[1]) != pos:  # make sure it isn't the same number we're checking for by comparing coords
                return False

        for j in range(9):
            if board[pos[0]][j] == num and (pos[0], j) != pos:  # Same row but not same number
                return False

        start_i = pos[0] - pos[0] % 3  # ex. 5-5%3 = 3 and thats where the grid starts
        start_j = pos[1] - pos[1] % 3
        for i in range(3):
            for j in range(3):  # adds i and j as needed to go from start of grid to where we need to be
                if board[start_i + i][start_j + j] == num and (start_i + i,
                                                               start_j + j) != pos:
                    return False
        return True

    def solve(board):
        '''Solves the Sudoku board via the backtracking algorithm'''

        empty = find_empty(board)
        if not empty:  # no empty spots are left so the board is solved
            return True

        for nums in range(9):
            if valid(board, empty, nums + 1):
                board[empty[0]][empty[1]] = nums + 1

                if solve(board):  # recursive step
                    return True
                board[empty[0]][empty[1]] = 0  # this number is wrong so we set it back to 0
        return False

    a1 = pmd[0]
    a2 = pmd[1]
    a3 = pmd[2]
    a4 = pmd[3]
    a5 = pmd[4]
    a6 = pmd[5]
    a7 = pmd[6]
    a8 = pmd[7]
    a9 = pmd[8]
    board = [
        a1, a2, a3, a4, a5, a6, a7, a8, a9
    ]
    solve(board)
    return print_board(board)
