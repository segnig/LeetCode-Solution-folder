class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        copy_nums = nums.copy()
        copy_nums.sort()

        first_indexs = {}
        for idx, num in enumerate(copy_nums):
            if num not in first_indexs:
                first_indexs[num] = idx

        for i, num in enumerate(nums):
            nums[i] = first_indexs[num]

        return nums   