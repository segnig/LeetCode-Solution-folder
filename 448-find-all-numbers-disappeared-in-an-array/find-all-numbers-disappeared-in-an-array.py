class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            while nums[i] != i + 1:
                correct_position = nums[i] - 1
                if nums[i] == nums[correct_position]:
                    break
                nums[i], nums[correct_position] = nums[correct_position], nums[i]

        for i in range(len(nums)):
            if nums[i] != i + 1:
                result.append(i + 1)
        return result