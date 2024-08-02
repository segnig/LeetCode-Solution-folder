class Solution:  
    def minSwaps(self, nums: List[int]) -> int:  
        count_ones = nums.count(1)  
        if count_ones <= 1:  # 0 or 1 ones need 0 swaps  
            return 0  

        nums = nums * 2  # doubling the array for circular behavior  
        max_ones_window = 0  
        current_ones = 0  # Number of 1s in the current window  

        # Initial window 
        n = len(nums)
        for i in range(count_ones):  
            if nums[i] == 1:  
                current_ones += 1  
        
        max_ones_window = current_ones  

        # Slide the window  
        for i in range(count_ones, n):  
            # Remove the leftmost element of the window  
            if nums[i - count_ones] == 1:  
                current_ones -= 1  
            # Add the new rightmost element to the window  
            if nums[i] == 1:  
                current_ones += 1  
            
            max_ones_window = max(max_ones_window, current_ones)  

        # Number of swaps required is total ones minus max ones in a window  
        return count_ones - max_ones_window