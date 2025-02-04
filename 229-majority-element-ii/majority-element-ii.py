class Solution(object):
    def majorityElement(self, nums):
        threshold = ceil(len(nums) / 3)
        counter_nums = Counter(nums)
        result = []

        for num in counter_nums:
            if counter_nums[num] > threshold:
                result.append(num)

        return result