class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        mx = max(nums)

        for i in range(1, mx + 1):
            if i not in nums:
                return i
        return mx + 1 if mx > 0 else 1