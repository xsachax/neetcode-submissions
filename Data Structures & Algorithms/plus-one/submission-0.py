class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        i = 0
        while i < len(digits):
            prev = digits[i]
            digits[i] = (digits[i] + 1) % 10
            if prev != 9:
                break
            elif i == len(digits)-1:
                digits.append(1)
                break
            i+=1
        digits.reverse()
        return digits