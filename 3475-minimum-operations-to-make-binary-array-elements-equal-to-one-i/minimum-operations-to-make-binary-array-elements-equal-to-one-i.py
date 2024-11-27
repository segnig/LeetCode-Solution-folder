from typing import List  

class Solution:  
    def minOperations(self, nums: List[int]) -> int:  
        count = 0  
        N = len(nums)  
        left = 0  

        while left + 2 < N:  
            while left < N and nums[left] == 1:  
                left += 1   
              
            if left + 2 < N:  
                # Perform operations  
                nums[left] = 1   
                nums[left + 1] = 1 if nums[left + 1] == 0 else 0  
                nums[left + 2] = 1 if nums[left + 2] == 0 else 0 
                left += 1
                count += 1
                while left < N and nums[left] == 1:  
                    left += 1

            else:
                break

        return -1 if left < N else count