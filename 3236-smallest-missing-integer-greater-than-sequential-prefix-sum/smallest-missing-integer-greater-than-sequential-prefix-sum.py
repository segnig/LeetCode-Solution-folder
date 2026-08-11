class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        result = nums[0]

        i = 0
        while i < len(nums) - 1 and nums[i + 1] == nums[i] + 1:
            i += 1
            result += nums[i]

        nums_set = set(nums)

        while result in nums_set:
            result += 1

        return result