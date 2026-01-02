class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        counter = {val: key for key, val in Counter(nums).items()}

        return counter[n]