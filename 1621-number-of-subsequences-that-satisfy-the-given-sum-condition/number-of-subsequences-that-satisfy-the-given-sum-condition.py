class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()

        result = 0
        right = len(nums) - 1

        for left, left_val in enumerate(nums):
            while left_val + nums[right] > target and left <= right:
                right -= 1
            if left <= right:
                result += 2 ** (right - left)
                result %= (10**9 + 7)
        return int(result)
        