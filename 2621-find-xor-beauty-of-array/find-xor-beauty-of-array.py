class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= ((num | num) & num)
        return result
        