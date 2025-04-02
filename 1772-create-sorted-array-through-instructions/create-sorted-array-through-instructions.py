class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums = []
        MOD = 1000000007
        result = 0
        for num in instructions:
            left = bisect_left(nums, num)
            right = bisect_right(nums, num)
            result += min(left, len(nums) - right)
            result %= MOD
            insort_left(nums, num)
        return result
