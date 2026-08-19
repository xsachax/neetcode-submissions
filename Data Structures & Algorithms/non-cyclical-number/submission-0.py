class Solution:
    def isHappy(self, n: int) -> bool:
        curr = n
        for i in range(1000):
            t=0
            for d in str(curr):
                t += int(d)**2
            if t == 1:
                return True
            curr = t
        return False