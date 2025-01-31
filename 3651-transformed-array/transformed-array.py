class Solution(object):
    def constructTransformedArray(self, nums):
        result = [0 for i in range(len(nums))]

        for i in range(len(nums)):
            result[i] = nums[(nums[i] + i) % len(nums)]
        return result
        