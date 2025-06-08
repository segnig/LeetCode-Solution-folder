class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        left = 0
        subarray_count = 0
        max_num_count = 0

        for right in range(len(nums)):
            max_num_count += nums[right] == max_element
            
            while max_num_count == k:
                max_num_count -= nums[left] == max_element
                left += 1
            subarray_count += left
        
        return subarray_count