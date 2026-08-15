class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:

        result = 0
        count_xor_been_zero = 0
        for num in nums:
            result ^= num
            count_xor_been_zero += result == 0
        
        if len(nums) == count_xor_been_zero:
            return 0

        return len(nums) if result else len(nums) - 1