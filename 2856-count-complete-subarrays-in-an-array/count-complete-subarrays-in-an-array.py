from collections import defaultdict  

class Solution(object):  
    def countCompleteSubarrays(self, nums):  
        count_dist = defaultdict(int)  
        left, right = 0, 0  
        L = len(set(nums))  
        result = 0  

        while right < len(nums):  
           
            count_dist[nums[right]] += 1  
            while len(count_dist) == L:  
                result += (len(nums) - right) 
                count_dist[nums[left]] -= 1   
                if count_dist[nums[left]] == 0:  
                    del(count_dist[nums[left]])  
                left += 1   

            right += 1 

        return result