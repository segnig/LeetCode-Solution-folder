class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globmax, globmin = nums[0], nums[0]
        curmin, curmax = 0, 0
        total = 0

        for num in nums:
            curmin = min(curmin + num, num)
            curmax = max(curmax + num, num)
            total += num
            globmax = max(globmax, curmax)
            globmin = min(globmin, curmin)
        
        return globmax if globmax < 0 else max(total - globmin, globmax)