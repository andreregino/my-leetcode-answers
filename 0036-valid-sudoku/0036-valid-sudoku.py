class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = {}
        rows = {}
        squares = {}

        for r in range(9):
            if r not in rows: # initializing rows
                rows[r] = set()
            for c in range(9):
                if c not in cols: # initializing columns
                    cols[c] = set()
                if (r, c) not in squares: # initializing squares
                    squares[(r, c)] = set()

                    
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True