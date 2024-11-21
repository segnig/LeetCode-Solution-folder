class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        left, right = 0, 1 

        result = 0

        diff = [nums[i] - nums[i - 1] for i in range(1, len(nums), 1)]

        while right < len(diff):
            if diff[right] == diff[left]:
                right += 1
            else:
                left, right = right, right + 1
            
            result += right - left - 1 if right - left > 1 else 0
            

        return result