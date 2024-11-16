class Solution(object):
    def resultsArray(self, nums, k):
        res= []
        
        for i in range(len(nums) - k + 1):
            result = nums[i]
            for j in range(i, i+k - 1, 1):
                if nums[j] + 1 != nums[j + 1]:
                    result = -1
            result = result if result == -1 else nums[i + k - 1]
            res.append(result)

        return res