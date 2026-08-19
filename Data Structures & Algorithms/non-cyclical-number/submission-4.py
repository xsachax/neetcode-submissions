class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            t=0
            while n:
                d = n%10
                t+= d**2
                n = n //10
            n=t
        return n == 1