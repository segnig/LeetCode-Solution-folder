class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(indx=0, comb=[]):
            if indx == len(nums):
                result.append(comb[:])
                return 
            comb.append(nums[indx])
            backtrack(indx+1, comb)
            comb.pop()
            backtrack(indx+1, comb)
        
        backtrack()

        return result