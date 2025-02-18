class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        pre_sum = [nums[0]]
        for i in range(1, len(nums)):
            pre_sum.append(pre_sum[-1] + nums[i])
        
        post_sum = [0 for _ in range(len(nums))]
        post_sum[-1] = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            post_sum[i] = (post_sum[i+ 1] + nums[i])
    
        for i in range(0, len(nums) - 1):
            if i == 0:
                if post_sum[1] == 0:
                    return 0
            elif post_sum[i + 1] == pre_sum[i-1]:
                
                return i
        
        if pre_sum[-2] == 0:
            
            return len(nums) - 1
        
        return -1