class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)

        for i in range(1, 102):
            if int(i * k) not in nums:
                return int(i * k)
        