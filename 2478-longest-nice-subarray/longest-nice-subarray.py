class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        result = 0
        bitmask = 0

        left = 0

        for right in range(len(nums)):
            while bitmask & nums[right] != 0:
                bitmask ^= nums[left]
                left += 1
            result = max(result, right - left + 1)
            bitmask |= nums[right]
        
        return result