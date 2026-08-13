import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        seen = set()
        pq = [[grid[0][0], 0, 0]]
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while pq:
            t, r, c = heapq.heappop(pq)
            if r in range(ROWS) and c in range(COLS) and (r,c) not in seen:
                seen.add((r, c))
                if r == ROWS-1 and c == COLS-1:
                    return t
                for dr, dc in DIRECTIONS:
                    if r+dr in range(ROWS) and c+dc in range(COLS):
                        heapq.heappush(pq, [max(t, grid[r+dr][c+dc]), r+dr, c+dc])
