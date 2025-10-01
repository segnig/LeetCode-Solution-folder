# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         if sum(nums) % 2 == 1:
#             return False
#         target = sum(nums) / 2

#         @cache
#         def dp(idx, sub1):
#             if idx == len(nums):
#                 return target == sub1
            

#             return dp(idx + 1, sub1 + nums[idx]) or dp(idx + 1, sub1)

#         return dp(0, 0)

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        
        @cache
        def dfs(i, rem):
            if rem == 0:
                return True
            if i >= len(nums) or rem < 0:
                return False
            
            return dfs(i + 1, rem) or dfs(i + 1, rem - nums[i])

        return dfs(0, target)
