class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= max_int else ~(a ^ mask)


# Actual one that works in Java but not python for some reason
# class Solution:
#     def getSum(self, a: int, b: int) -> int:
#         while b != 0:
#             carry = (a&b) << 1
#             a ^=b
#             b = carry
#         return a
