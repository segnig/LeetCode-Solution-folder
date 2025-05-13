class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)

        sum_total = (n * (n + 1)) // 2
        return sum_total - total