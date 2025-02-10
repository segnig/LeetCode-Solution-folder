class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if int(str(nums[i]) + str(nums[j])) < int(str(nums[j]) + str(nums[i])):
                    nums[i], nums[j] = nums[j], nums[i]
        nums = [str(n) for n in nums]
        return str(int("".join(nums)))
        