class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[_]] for _ in range(len(nums))]