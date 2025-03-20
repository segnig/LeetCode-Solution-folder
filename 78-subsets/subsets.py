class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(indx=0, comb=[]):
            if indx == len(nums):
                result.append(comb)
                return 
            
            backtrack(indx+1, comb)
            backtrack(indx+1, comb + [nums[indx]])
        
        backtrack()

        return result