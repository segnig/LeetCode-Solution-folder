class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for indx in range(len(nums) - 1):
            if nums[indx] == nums[indx + 1]:
                nums[indx], nums[indx + 1] = 2* nums[indx], 0

        result = [0 for _ in range(len(nums))]

        indx = 0

        for num in nums:
            if num != 0:
                result[indx] = num
                indx += 1

        return result
        