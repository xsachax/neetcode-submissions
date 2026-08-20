from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.p = defaultdict(int)
        
        

    def add(self, point: List[int]) -> None:
        self.p[tuple(point)]+=1
        

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0
        for (x, y), diag_count in self.p.items():
            if (abs(py - y) != abs(px - x)) or x == px or y == py: #  any diagonal point
                continue
            res += (diag_count * self.p.get((x, py), 0) * self.p.get((px, y), 0))
        return res

