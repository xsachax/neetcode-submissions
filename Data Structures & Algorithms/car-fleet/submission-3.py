class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        pairs = list(zip(position, speed))
        pairs.sort(reverse=True)
        anchor = -1
        for pair in pairs:
            t = (target-pair[0]) / pair[1]
            if t > anchor:
                fleets+=1
                anchor = t
        return fleets
