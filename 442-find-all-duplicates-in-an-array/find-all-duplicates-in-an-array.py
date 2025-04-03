class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = set()

        for i in range(len(nums)):
            while nums[i] != i + 1:
                correct_position = nums[i] - 1
                if nums[i] == nums[correct_position]:
                    result.add(nums[i])
                    break
                nums[i], nums[correct_position] = nums[correct_position], nums[i]

        return list(result)