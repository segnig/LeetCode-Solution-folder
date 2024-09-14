class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        mx_num = max(nums)

        result, count = 0, 0


        for n in nums:
            if n == mx_num:
                count += 1
            else:
                count = 0

            result = max(result, count)

        return result


        