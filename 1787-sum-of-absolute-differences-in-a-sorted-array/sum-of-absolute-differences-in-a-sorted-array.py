class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix_sum = [0]

        for num in nums:
            prefix_sum.append(num + prefix_sum[-1])

        result = []

        for i in range(1, len(nums) + 1):
            left = prefix_sum[i-1]
            right = prefix_sum[-1] - left
            result.append(((i - 1) * nums[i - 1] - left) + (right - ((len(nums) - i + 1) * nums[i - 1])))
    
        return result
