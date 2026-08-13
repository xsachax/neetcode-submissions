class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        def jump(i) -> bool:
            if i >= len(nums)-1:
                return True
            elif nums[i] == 0:
                return False
            else:
                return False or any(jump(i + x) for x in range(1, nums[i] + 1))
            
        return jump(0)