class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subsets = []

        def backtrack(start, subset):
            subsets.append(subset[:]) 
            for k in range(start, len(nums)):
                subset.append(nums[k])
                backtrack(k+1, subset)
                subset.pop()
                
        backtrack(0, [])
        return subsets
        