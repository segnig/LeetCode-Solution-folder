class Solution:  
    def countValidSelections(self, nums: List[int]) -> int:  
        total_sum = sum(nums)  
        prefix_sum = [0]  

        for n in nums:  
            prefix_sum.append(prefix_sum[-1] + n)  

        result = 0  

        # Iterate through the prefix sums  
        for n in range(1, len(prefix_sum)):  
            if prefix_sum[-1] - 2 * prefix_sum[n] == 0 and nums[n - 1] == 0:  
                result += 2   
            elif (prefix_sum[-1] - prefix_sum[n] == prefix_sum[n] - 1 or   
                  prefix_sum[-1] - prefix_sum[n] == prefix_sum[n] + 1) and nums[n - 1] == 0:  
                result += 1  
        
        return result