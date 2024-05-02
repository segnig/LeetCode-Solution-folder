class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        right = len(nums) - 1
        left = 0
        while left < right:
            if nums[right] + nums[left] == 0:
                return nums[right]
            if nums[right] + nums[left] > 0:
                right -= 1
            else:
                left += 1
        return -1