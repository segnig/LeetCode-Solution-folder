class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counter_nums = Counter(nums)

        pairs, remains = 0, 0

        for num in counter_nums:
            pairs += counter_nums[num] // 2
            remains += counter_nums[num] % 2

        return [pairs, remains]