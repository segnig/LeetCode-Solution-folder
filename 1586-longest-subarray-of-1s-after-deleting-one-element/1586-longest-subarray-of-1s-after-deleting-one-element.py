class Solution(object):
    def longestSubarray(self, nums):
        count = 0

        left, right = 0, 0

        result = 0

        if 0 not in nums:
            return len(nums) - 1

        while right < len(nums):
            while count > 1:
                if nums[left] == 0:
                    count -= 1
                left += 1

            while right <  len(nums) and count < 2:
                if nums[right] == 0:
                    count += 1

                result = max(result, right - left - count)
                right += 1
            result = max(result, right - left - count)
        return result