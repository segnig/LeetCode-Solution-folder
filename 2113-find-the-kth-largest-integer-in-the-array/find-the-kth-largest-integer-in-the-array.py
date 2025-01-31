class Solution(object):
    def kthLargestNumber(self, nums, k):
        sorted_nums = sorted(nums, key=lambda x: int(x))
        return sorted_nums[-k]
        