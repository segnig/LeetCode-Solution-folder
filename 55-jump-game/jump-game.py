class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_steps = 0
        for i in range(len(nums)):
            if nums[i] == 0 and max_steps <= i and i < len(nums) - 1:
                return False
            max_steps = max(max_steps, nums[i] + i)

        return True