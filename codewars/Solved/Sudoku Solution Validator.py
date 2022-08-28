def valid_solution(board):
    for x in range(len(board)):
        if x <= 3:
            start = 0
            end = 3
        elif x <= 6:
            start = 3
            end = 6
        elif x <= 9:
            start = 6
            end = 9
            
        test_row = set()
        test_column = set()
        test_grid = set()
        for y in range(len(board)):
            if board[x][y] in test_row or board[x][y] == 0:
                return False
            else:
                test_row.add(board[x][y])

            if board[y][x] in test_column or board[y][x] == 0:
                return False
            else:
                test_column.add(board[y][x])

        for a in range(start, end):
            for b in range(start, end):
                if board[a][b] in test_grid:
                    return False
                else:
                    test_grid.add(board[a][b])
    return True

ans = valid_solution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
])
print(ans)