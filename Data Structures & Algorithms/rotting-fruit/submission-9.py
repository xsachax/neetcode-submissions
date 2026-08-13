from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        q = deque()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append((r, c))


        while q and fresh>0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    if r+dr in range(ROWS) and c+dc in range(COLS) and grid[r+dr][c+dc] == 1:
                        fresh-=1
                        grid[r+dr][c+dc] = 2
                        q.append((r+dr, c+dc))
            time+=1





        return time if fresh == 0 else -1


































        # rows = len(grid)
        # cols = len(grid[0])
        # q = collections.deque()

        # fresh = 0
        # time = 0

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 1:
        #             fresh+=1
        #         elif grid[r][c] == 2:
        #             q.append((r, c))

        # directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # while q and fresh > 0:
        #     l = len(q)
        #     for _ in range(l):
        #         r, c = q.popleft()
        #         for dr, dc in directions:
        #             nextRow = r+dr
        #             nextCol = c+dc
        #             if nextRow in range(rows) and nextCol in range(cols) and grid[nextRow][nextCol] == 1:
        #                 grid[nextRow][nextCol] = 2
        #                 fresh-=1
        #                 q.append((nextRow, nextCol))
        #     time+=1
        
        # if fresh != 0:
        #     return -1
        # else:
        #     return time








