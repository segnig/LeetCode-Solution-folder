class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        result = 0

        while right < len(nums):
            while right < len(nums) and  (k > 0 or nums[right] == 1):
                if nums[right] == 0:
                    k -= 1
                right += 1
                result = max(right - left, result)
                
            if left < len(nums) and nums[left] == 0:
                k += 1
            left += 1

        return result