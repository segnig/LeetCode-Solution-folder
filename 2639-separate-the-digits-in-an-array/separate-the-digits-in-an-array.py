class Solution(object):
    def separateDigits(self, nums):
        return [int(n) for num in nums for n in str(num)]
        