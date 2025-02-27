class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_sum = 0
        max_sum = 0
        result = 0
        running_sum = 0
        for num in nums:
            running_sum += num
            result = max(abs(running_sum - min_sum), abs(max_sum - running_sum), result)
            max_sum = max(max_sum, running_sum)
            min_sum = min(min_sum, running_sum)
        return result
        