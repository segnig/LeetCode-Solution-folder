class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subsets = set()
        
        def backtrack(i, subset):
            nonlocal subsets
            if i == len(nums):
                subsets.add(tuple(subset[::]))
                return
            
            for k in range(i, len(nums)):
                subset.append(nums[k])
                backtrack(k+1, subset)
                subset.pop()
                backtrack(k+1, subset)


        backtrack(0, [])

        return [list(subset) for subset in subsets]
        