class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        N = len(nums)
        if N == 1:
            return nums

        nums = Counter(nums)
        target = N / 3
        result = [v for v, c in nums.items() if c > target]

        return result