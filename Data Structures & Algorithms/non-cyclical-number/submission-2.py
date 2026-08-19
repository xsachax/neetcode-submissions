class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            t = sum([int(d)**2 for d in str(n)])
            n=t

        return n == 1