class Solution(object):  
    def maximumSubarraySum(self, nums, k):  
        stores = set()  
        result, cur_sum = 0, 0  
        left, right = 0, 0  
        
        while right < len(nums):  
              
            cur_sum += nums[right] 
            while nums[right] in stores:
                cur_sum -= nums[left]  
                stores.remove(nums[left]) 
                left += 1
            stores.add(nums[right])  
            right += 1  
            
             
            while len(stores) > k:  
                cur_sum -= nums[left]  
                stores.remove(nums[left])  
                left += 1  
            
           
            if len(stores) == k:  
                result = max(result, cur_sum)  

        return result