class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        placeholder = 1
        for seeker in range(1, len(nums)):
            if nums[placeholder - 1] != nums[seeker]:
                nums[placeholder] = nums[seeker]
                placeholder += 1
        return placeholder 