class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counter_nums = Counter(nums)

        result = []

        for num in counter_nums:
            if counter_nums[num] > 1:
                result.append(num)

        return result