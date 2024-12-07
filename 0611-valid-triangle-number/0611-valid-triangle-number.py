class Solution(object):
    def triangleNumber(self, nums):
        
        nums.sort() 
        result = 0

        for x in range(2, len(nums)):
            left = 0
            right = x - 1

            while left < right:
                if nums[left] + nums[right] > nums[x]:
                    result += right - left
                    right -= 1
                else:
                    left += 1
            
        return result


