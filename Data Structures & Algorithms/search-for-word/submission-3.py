class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            
            if r in range(ROWS) and c in range(COLS) and board[r][c] == word[i] and (r,c) not in visited:
                visited.add((r, c))
                res = any(dfs(r+dr, c+dc, i+1) for dr,dc in DIRECTIONS)
                visited.remove((r, c))
                return res
        

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True
        return False