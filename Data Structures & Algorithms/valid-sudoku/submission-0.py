class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        combos = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    el = board[i][j]
                    combos += [("row", el, i), ("col", el, j), ("square", el, i//3, j//3)]

        return len(combos) == len(set(combos))
