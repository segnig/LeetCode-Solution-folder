class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        
        left, right = 0, 1
        result = max(nums)
        
        for right in range(1, len(prefix_sum)):
            if prefix_sum[right] - prefix_sum[left] < 0:
                left = right
            else:
                result = max(result, prefix_sum[right] - prefix_sum[left])
        return result