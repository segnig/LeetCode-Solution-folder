class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = sum(nums[:k]) / k
        sum_window = sum(nums[:k])
        for i in range(k, len(nums)):
            sum_window += nums[i] - nums[i - k] 
            result = max(sum_window / k, result)
        return result