class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result =0 
        total = nums[0]
        right = 1
        result = max(result, total)
        while right < len(nums):
            if nums[right - 1] < nums[right]:
                total += nums[right]
                result = max(result, total)
            else:
                total = nums[right]
            right += 1
        result = max(result, total)
        return result 
         