class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        anchor = -1
        for p, s in pairs:
            t = (target-p) / s
            if t > anchor:
                fleets+=1
                anchor = t
        return fleets
