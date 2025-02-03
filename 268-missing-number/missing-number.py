class Solution(object):
    def missingNumber(self, nums):
        mx = max(nums)
        nums = set(nums)
        for i in range(mx + 2):
            if i not in nums:
                return i