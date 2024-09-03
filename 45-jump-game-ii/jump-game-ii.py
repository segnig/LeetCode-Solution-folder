class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = right = 0

        result = 0

        while right <  len(nums) - 1:
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, i  + nums[i])

            left = right + 1
            right = farthest
            result += 1
        return result   